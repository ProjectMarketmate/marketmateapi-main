from django.contrib import admin

from core.models import CartItem, OfferBanner, Order, Product, Category

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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
 pass

@admin.register(OfferBanner)
class BannerAdmin(admin.ModelAdmin):
 pass