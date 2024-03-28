from rest_framework import serializers

from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from core.api.app.rating import RatingSerializer
from core.models import Category, Product


from core.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        





class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['category']
    search_fields = ['name']
    