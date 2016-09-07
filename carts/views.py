from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from products.models import Variation
from carts.models import Cart, CartItem

# Create your views here.


class CartView(View):

    def get(self, request, *args, **kwargs):
        item_id = request.GET.get('item')
        delete_item = request.GET.get('delete')
        if item_id:
            item_instance = get_object_or_404(Variation, id=item)
            qty = request.GET.get('qty')
            cart = Cart.objects.all()[0]
            cart_item = CartItem.objects.get_or_create(cart=cart, item=item_instance)[0]
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
        return HttpResponseRedirect('/')
