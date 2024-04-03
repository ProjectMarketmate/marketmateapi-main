import random
from django.http import JsonResponse
from core.models import OrderItem, Product
from core.api.app.product import ProductSerializer

def get_recommendations(request):
    # Retrieve all orders
    all_orders = OrderItem.objects.all()
    
    # Extract products from each order
    all_products = [order_item.product for order_item in all_orders]
    
    # Shuffle the list of products to randomize their order
    random.shuffle(all_products)
    
    # Convert each product to its serialized form
    serialized_products = [ProductSerializer(product).data for product in all_products]
    
    return JsonResponse({'recommendations': serialized_products})
