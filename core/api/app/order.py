import random
from urllib import request
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import CustomUser
from core.api.app.product import ProductSerializer
from core.models import CartItem, Order, OrderItem, Product
from rest_framework import generics


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
        request = self.context.get('request')
        items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(items, many=True,context={'request': request})
        return serializer.data

class OrderApiView(APIView):
    def get(self, request, *args, **kwargs):
        userId = request.user.id
        if userId:
            orders = Order.objects.filter(user=userId)
            serializer = OrderSerializer(orders, many=True,context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class OrderCreateApiView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        order = Order.objects.create(user=user)
        cart_items = CartItem.objects.filter(user=user)
        staffs = CustomUser.objects.filter(is_staff=True,is_active=True,is_superuser=False)

        random_staff = staffs[random.randint(0, len(staffs) - 1)]
        if random_staff:
            order.staff = random_staff
            order.save()          
        
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
            cart_item.delete()

        return Response(status=status.HTTP_201_CREATED)

# class OrderDeleteApiView(APIView):
#     def delete(self, request, pk, *args, **kwargs):
#         userId = request.user.id
#         if userId:
#             try:
#                 order = Order.objects.get(id=pk, user=request.user)
#             except Order.DoesNotExist:
#                 return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

#             order.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer