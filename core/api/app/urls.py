from django.urls import path

from core.api.app.product import ProductListAPIView
from core.api.app.cart import CartItemListApiView

urlpatterns=[
  path('products/',ProductListAPIView.as_view(),name="app-products"),
  path('cart/',CartItemListApiView.as_view()),
  

]