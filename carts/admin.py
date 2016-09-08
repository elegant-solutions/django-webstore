#Importing resources
from django.contrib import admin

#Registering our Models
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)
