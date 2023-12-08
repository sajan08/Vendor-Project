from django.db import models

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.TextField()

    def _str_(self):
        return self.name

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50)
    order_date = models.DateField()
    items = models.TextField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20)

    def _str_(self):
        return f"{self.vendor.name} - {self.po_number}"
