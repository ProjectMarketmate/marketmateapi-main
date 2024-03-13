from rest_framework import serializers
from core.api.app.product import ProductSerializer

from core.models import CartItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CartItemGetSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'

class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

 
    
class CartItemListApiView(APIView):

    
    def get(self, request, *args, **kwargs):
        userId = request.user.id
        if userId:
            cart_items = CartItem.objects.filter(user=userId)
            serializer = CartItemGetSerializer(cart_items, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
     
        serializer = CartItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       