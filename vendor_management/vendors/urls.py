# vendors/urls.py
from django.urls import path
from .views import PurchaseOrderListCreateView, PurchaseOrderDetailView
from .views import VendorListCreateView, VendorDetailView

urlpatterns = [
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
]
