from urllib import request
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.api.app.product import ProductSerializer
from core.models import CartItem, Order, OrderItem, Product



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['user','status','created_at','updated_at','items','id']

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

class OrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        userId = request.user.id
        if userId:
            orders = Order.objects.filter(user=userId)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class OrderCreateApiView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        order = Order.objects.create(user=user)
        cart_items = CartItem.objects.filter(user=user)

        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
            cart_item.delete()

        return Response(status=status.HTTP_201_CREATED)
