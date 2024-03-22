from django.urls import path

from core.api.app.order import OrderRetrieveUpdateDestroyAPIView
from core.api.delivery.orders import OrderListCreateAPIView



urlpatterns=[
  path('orders/', OrderListCreateAPIView.as_view()),
  path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view()),
  

]