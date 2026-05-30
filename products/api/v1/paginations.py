from rest_framework.pagination import PageNumberPagination
from products.models.products import Product

class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    max_page_size = 100
