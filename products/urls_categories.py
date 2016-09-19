from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import CategoryListView, CategoryDetailView

# =========================================================================
# Enabling RESTful architecture with dynamic urls.
# Overall url patterns for the categories page within the products app.
# =========================================================================

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='categories'),
    url(r'^(?P<slug>[\w-]+)/?$', CategoryDetailView.as_view(), name='category_detail'),
]
