"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from carts.views import CartView, ItemCountView, CheckoutView, CheckoutFinalView
from invoice.views import (
                        AddressSelectFormView,
                        UserAddressCreateView,
                        OrderList,
                        UserCheckoutAPI,
                        OrderDetail
                        )
from products.views import (
                        APIHomeView,
                        CategoryListAPIView,
                        CategoryRetrieveAPIView,
                        ProductListAPIView,
                        ProductRetrieveAPIView,
                        )
# =========================================================================
# Enabling RESTful architecture with dynamic urls.
# Overall url patterns for webstore.
# =========================================================================
urlpatterns = [
    url(r'^$', 'subscribers.views.home', name='home'),
    url(r'^about/$', 'webstore.views.about', name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressSelectFormView.as_view(), name='checkout_address'),
    url(r'^checkout/address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),

]

#API Patterns
urlpatterns += [
    url(r'^api/$', APIHomeView.as_view(), name='home_api'),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth/token/refresh$', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/categories/$', CategoryListAPIView.as_view(), name='categories_api'),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
    url(r'^api/products/$', ProductListAPIView.as_view(), name='products_api'),
    url(r'^api/products/(?P<pk>\d+)/$', ProductRetrieveAPIView.as_view(), name='product_detail_api'),
    url(r'^api/user/checkout/$', UserCheckoutAPI.as_view(), name='user_checkout_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
