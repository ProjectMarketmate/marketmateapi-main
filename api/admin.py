from django.contrib import admin

from api.models import Order, OrderItem, Payment, Product, User, Category

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 pass 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 pass 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
 pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
 pass 

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
 pass 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
 pass 


admin.site.site_header = "MarketMate"
admin.site.site_title = "MarketMate"
