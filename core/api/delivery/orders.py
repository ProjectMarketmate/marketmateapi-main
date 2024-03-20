from core.models  import Order
from rest_framework import serializers
from rest_framework import generics
from rest_framework import serializers
from core.models import Order, OrderItem
from django_filters.rest_framework import DjangoFilterBackend

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
 
    class Meta:
        model = Order
        fields = ['user', 'status', 'items']


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    


# class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer