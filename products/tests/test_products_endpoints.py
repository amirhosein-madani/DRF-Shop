import pytest
from rest_framework.test import APIClient
from accounts.models import User
from django.urls import reverse
from products.models.products import Product

# from products.models.categories import Category


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def admin_user():
    user = User.objects.create_superuser(
        username="amir",
        password="amirmad2007",
        email="amirmadani901@gmail.com",
        phone_number="09912038679",
    )
    return user


@pytest.fixture
def normal_user():
    user = User.objects.create_user(
        username="normal",
        password="amirmad2007",
        email="example@gmail.com",
        phone_number="09125179954",
    )
    return user


@pytest.mark.django_db
class TestProductApi:

    def test_product_list_respomse_200_status(self, api_client):
        url = reverse("product-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_product_without_user_respomse_401_status(self, api_client):
        url = reverse("product-list")
        data = {}
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_product_with_normal_user_respomse_403_status(
        self, api_client, normal_user
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse("product-list")
        data = {}
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_product_with_amin_user_respomse_400_status(
        self, api_client, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("product-list")
        data = {}
        response = api_client.post(url, data)
        assert response.status_code == 400
