from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from products import views


urlpatterns = [
    path('products/',views.ListProductsView.as_view(), name='products-all')
]
