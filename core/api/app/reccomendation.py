from django.http import JsonResponse
from core.models import OrderItem
from collections import Counter

def get_recommendations(request, userId):
    # Get all orders of the user
    user_orders = OrderItem.objects.filter(order__user_id=userId)
    
    # Extract product names from order items
    products = [order_item.product.name for order_item in user_orders]
    
    # Count the frequency of each product
    product_counts = Counter(products)
    
    # Sort products by frequency in descending order
    sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Get top 3 recommended products for the customer
    recommendations = [product[0] for product in sorted_products[:3]]
    return JsonResponse({'recommendations': recommendations})




