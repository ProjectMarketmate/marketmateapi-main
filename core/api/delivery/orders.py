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
        fields = ['user', 'status', 'items','id']


class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(staff=user)
    
class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()