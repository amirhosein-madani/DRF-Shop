from rest_framework import viewsets

from products.models.products import Product
from .serializers import ProductSerializer
from .paginations import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from accounts.api.v1.permissions import IsAdminOrReadOnly


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category", "color", "size"]
    search_fields = ["title", "description"]
