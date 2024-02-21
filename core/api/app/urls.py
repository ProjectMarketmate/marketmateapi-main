from django.urls import path

from core.api.app.product.views import ProductListAPIView



urlpatterns=[
  path('products/',ProductListAPIView.as_view(),name="app-products")

]