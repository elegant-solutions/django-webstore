# Stdlib
from django.contrib import admin

# Django-Webstore
from .models import Cart, CartItem


# =========================================================================
# ----- Custom Admin Classes
# =========================================================================
class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]

    class Meta:
        model = Cart


# =========================================================================
# ----- Admin Model Registration
# =========================================================================
admin.site.register(Cart, CartAdmin)
