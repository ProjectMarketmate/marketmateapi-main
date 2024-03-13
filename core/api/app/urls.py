from django.urls import path

from core.api.app.product import CategoryListAPIView, ProductListAPIView
from core.api.app.cart import CartItemDeleteApiView, CartItemListApiView, CartItemUpdateApiView

urlpatterns=[
  path('products/',ProductListAPIView.as_view(),name="app-products"),
  path('cart/',CartItemListApiView.as_view()),
  path('cart/update/<int:pk>/',CartItemUpdateApiView.as_view()),
  path('cart/delete/<int:pk>/',CartItemDeleteApiView.as_view()),
  path('categories/',CategoryListAPIView.as_view()),
  
]