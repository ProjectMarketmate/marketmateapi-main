from rest_framework import generics
from core.api.app.product.serializers import ProductSerializer
from core.api.app.product.serializers import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.models import Category, Product

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['category']
    search_fields = ['name',]