from django.db import models
from django.utils import timezone


class Vendor(models.Model):
    vendor_code = models.CharField(max_length=20, unique=True)
    name = models.TextField()
    contact_details = models.CharField(max_length=255)
    address = models.TextField()
    
    # Performance Metrics
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    fulfilment_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def _str_(self):
        return self.name
    
    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        on_time_delivery_pos = completed_pos.filter(delivery_date__lte=timezone.now())
        
        total_completed_pos = completed_pos.count()
        on_time_delivery_count = on_time_delivery_pos.count()

        return (on_time_delivery_count / total_completed_pos) * 100 if total_completed_pos > 0 else 0.0

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        
        total_completed_pos = completed_pos.count()
        if total_completed_pos == 0:
            return 0.0

        on_time_delivery_count = completed_pos.filter(
            delivery_date__lte=timezone.now()
        ).aggregate(count=Count('pk'))['count']

        return (on_time_delivery_count / total_completed_pos) * 100

    def calculate_average_response_time(self):
        acknowledged_pos = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos]

        return sum(response_times) / len(response_times) if len(response_times) > 0 else 0.0

    def calculate_fulfilment_rate(self):
        successfully_fulfilled_pos = self.purchaseorder_set.filter(status='completed', issues__isnull=True)
        total_issued_pos = self.purchaseorder_set.count()

        return (successfully_fulfilled_pos.count() / total_issued_pos)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(default=timezone.now)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return f"{self.vendor.name} - {self.po_number}"
    
    def update_performance_metrics(self):
        if self.status == 'completed':
            self.vendor.on_time_delivery_rate = self.vendor.calculate_on_time_delivery_rate()
            self.vendor.quality_rating_avg = self.vendor.calculate_quality_rating_average()
            self.vendor.average_response_time = self.vendor.calculate_average_response_time()

        self.vendor.fulfillment_rate = self.vendor.calculate_fulfilment_rate()
        self.vendor.save()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"