from rest_framework import viewsets
from products.models.products import Product
from products.models.categories import Category
from products.models.sizes import Size
from products.models.colors import Color
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ColorSerializer,
    SizeSerializer,
)
from .paginations import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from accounts.api.v1.permissions import IsAdminOrReadOnly


class ProductModelViewSet(viewsets.ModelViewSet):
    """
    this is a ModelViewSet for ProductSerializer
    """

    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category", "color", "size"]
    search_fields = ["title", "description"]


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    this is a ModelViewSet for CategorySerializer
    """

    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer


class ColorModelViewSet(viewsets.ModelViewSet):
    """
    this is a ModelViewSet for ColorSerializer
    """

    queryset = Color.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ColorSerializer


class SizeModelViewSet(viewsets.ModelViewSet):
    """
    this is a ModelViewSet for SizeSerializer
    """

    queryset = Size.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = SizeSerializer
