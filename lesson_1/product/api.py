from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Product, Category
from .serializers import ProductSerializer


# class ProductsListAPI(ListViewSet, RetrieveAPIView):
class ProductsListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsRetriveAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
