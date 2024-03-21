from django.urls import include, path

from core.api.app.order import OrderApiView, OrderCreateApiView, OrderDeleteApiView, OrderRetrieveUpdateDestroyAPIView
from core.api.app.product import CategoryListAPIView, ProductListAPIView
from core.api.app.cart import CartItemDeleteApiView, CartItemListApiView, CartItemUpdateApiView
from core.api.delivery.orders import OrderRetrieveUpdateDestroyAPIView


urlpatterns=[
  path('products/',ProductListAPIView.as_view(),name="app-products"),
  path('cart/',CartItemListApiView.as_view()),
  path('cart/update/<int:pk>/',CartItemUpdateApiView.as_view()),
  path('cart/delete/<int:pk>/',CartItemDeleteApiView.as_view()),
  path('categories/',CategoryListAPIView.as_view()),
  path('order/',OrderApiView.as_view(),name="app-order"),
  path('order/create/',OrderCreateApiView.as_view(),name="app-order-create"),

  path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),

  
]