from django.contrib import admin

from core.models import CartItem, Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 pass 



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
 pass 

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
 pass

admin.site.site_header = "MARKETMATE"
admin.site.site_title = "MARKETMATE"
