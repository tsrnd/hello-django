from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer


class ListProductsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
