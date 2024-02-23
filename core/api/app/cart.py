from rest_framework import serializers
from rest_framework import generics
from core.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = CartItem
        fields = '__all__'
    
class CartItemListApiView(generics.ListAPIView):
    queryset= CartItem.objects.all()
    serializer_class = CartItemSerializer