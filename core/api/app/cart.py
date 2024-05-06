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
        user = request.user
        data = request.data.copy()
        data['user'] = user.id
        product_id = data.get('product') 
        
        # Check if the product already exists in the user's cart
        existing_cart_item = CartItem.objects.filter(user=user, product=product_id).first()
        if existing_cart_item:
            
            existing_cart_item.quantity += data.get('quantity', 1)
            existing_cart_item.save()
            serializer = CartItemCreateSerializer(existing_cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        #  product does not exist, create a new cart item
        serializer = CartItemCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CartItemUpdateApiView(APIView):

    def patch(self, request, pk, *args, **kwargs):
        userId = request.user.id
        if userId:
            try:
                cart_item = CartItem.objects.get(id=pk, user=request.user)
            except CartItem.DoesNotExist:
                return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

            quantity = request.data.get('quantity')
            cart_item.quantity = quantity
            cart_item.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class CartItemDeleteApiView(APIView):

    def delete(self, request, pk, *args, **kwargs):
        userId = request.user.id
        if userId:
            try:
                cart_item = CartItem.objects.get(id=pk, user=request.user)
            except CartItem.DoesNotExist:
                return Response({"error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
