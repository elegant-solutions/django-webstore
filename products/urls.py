from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import ProductDetailView, ProductListView

urlpatterns = [
    url(r'^(?P<pk>\d+)', ProductDetailView.as_view(), name='product_detail'),
    url(r'^$', ProductListView.as_view(), name='products'),
]
