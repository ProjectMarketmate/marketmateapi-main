from django.urls import path

from core.api.delivery.orders import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView



urlpatterns=[
  path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
  

]