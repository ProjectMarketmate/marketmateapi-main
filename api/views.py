from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.models import Order, OrderItem, Product, User
from api.serializers import OrderItemSerializer, OrderSerializer, ProductSerializer, UserSerializer


class UserListApiview(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserdetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ProductListApiview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductdetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderItemlistApiview(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer

class OrderItemDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderItemSerializer


class ProductCategoryFilterAPIView(APIView):
    
    def get(self, request, cat,):
        products = Product.objects.filter(category=cat)
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    


