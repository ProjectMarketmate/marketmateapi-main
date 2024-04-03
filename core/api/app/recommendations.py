# import random
# from django.http import JsonResponse
# from core.models import OrderItem, Product
# from core.api.app.product import ProductSerializer

# def get_recommendations(request):
    
#     all_orders = OrderItem.objects.all()
#     all_products = [order_item.product for order_item in all_orders]
#     random.shuffle(all_products)
#     serialized_products = [ProductSerializer(product).data for product in all_products]
    
#     return JsonResponse({'recommendations': serialized_products})


import random
from django.http import JsonResponse
from core.models import Product
from core.api.app.product import ProductSerializer

def get_recommendations(request):
    all_products = list(Product.objects.all())  # Convert QuerySet to a list
    
    random.shuffle(all_products)
    
    serialized_products = [ProductSerializer(product,context={'request': request}).data for product in all_products]
    
    return JsonResponse({'recommendations': serialized_products})

