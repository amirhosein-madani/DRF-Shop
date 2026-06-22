from django.urls import path
from .views import (
    CartAddGenericApiView,
    CartApiView,
    CartRemoveApiView,
    ClearCartApiView,
)

urlpatterns = [
    path("add-to-cart/", CartAddGenericApiView.as_view(), name="add_to_cart"),
    path("cart/", CartApiView.as_view(), name="cart"),
    path(
        "cart-remove-item/<int:product_id>/",
        CartRemoveApiView.as_view(),
        name="remove_item_from_cart",
    ),
    path("cart-clear/", ClearCartApiView.as_view(), name="cart_clear"),
]
