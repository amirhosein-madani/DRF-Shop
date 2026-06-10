import pytest
from django.urls import reverse
from accounts.tests.test_account_api import api_client, common_user  # noqa: F401
from products.tests.test_products_endpoints import random_product  # noqa: F401
from cart.cart import Cart


@pytest.fixture
def common_user_cart(common_user, random_product):

    cart = Cart(common_user.id)
    cart.add(
        product_id=random_product.id,
        quantity=2,
        price=random_product.price,
    )
    return cart


@pytest.mark.django_db
class TestCartApi:

    def test_cart_response_401_status(self, api_client):
        url = reverse("cart")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_add_to_cart_response_401_status(self, api_client):
        url = reverse("add_to_cart")
        response = api_client.post(url, {})
        assert response.status_code == 401

    def test_cart_clear_response_401_status(self, api_client):
        url = reverse("cart_clear")
        response = api_client.delete(url)
        assert response.status_code == 401

    def test_remove_item_from_cart_response_401_status(
        self, api_client, random_product
    ):
        url = reverse("remove_item_from_cart", kwargs={"product_id": random_product.pk})
        response = api_client.delete(url)
        assert response.status_code == 401

    def test_cart_response_200_status(self, api_client, common_user):
        api_client.force_authenticate(user=common_user)
        url = reverse("cart")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_cart_clear_response_204_status(self, api_client, common_user):
        api_client.force_authenticate(user=common_user)
        url = reverse("cart_clear")
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_add_to_cart_response_200_status(
        self, api_client, random_product, common_user, common_user_cart
    ):
        api_client.force_authenticate(user=common_user)
        url = reverse("add_to_cart")
        data = {
            "product_id": random_product.pk,
            "quantity": 4,
        }
        response = api_client.post(url, data)
        assert response.status_code == 200

    def test_add_to_cart_response_400_status(
        self, api_client, random_product, common_user, common_user_cart
    ):
        api_client.force_authenticate(user=common_user)
        url = reverse("add_to_cart")
        data = {
            "product_id": 1,
            "quantity": 4,
        }
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_remove_item_from_cart_response_204_status(
        self, api_client, random_product, common_user, common_user_cart
    ):
        api_client.force_authenticate(user=common_user)
        url = reverse("remove_item_from_cart", kwargs={"product_id": random_product.pk})
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_remove_item_from_cart_response_404_status(
        self, api_client, random_product, common_user, common_user_cart
    ):
        api_client.force_authenticate(user=common_user)
        url = reverse("remove_item_from_cart", kwargs={"product_id": 1})
        response = api_client.delete(url)
        assert response.status_code == 404
