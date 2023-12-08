from rest_framework import serializers
from .models import Vendor
from .models import PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'vendor_code', 'name', 'contact_details', 'address']
        

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'vendor', 'po_number', 'order_date', 'items', 'quantity', 'status']
        