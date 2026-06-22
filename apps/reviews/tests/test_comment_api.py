import pytest
from django.shortcuts import reverse
from rest_framework.test import APIClient
from accounts.models import User
from products.models.products import Product
from ..models import Comment


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
def random_product():
    product = Product.objects.create(
        title="test",
        price=100.00,
        description="test`111",
    )
    return product


@pytest.fixture
def normal_user():
    user = User.objects.create_user(
        username="normal",
        password="amirmad2007",
        email="example@gmail.com",
        phone_number="09125179954",
    )
    return user


@pytest.fixture
def another_admin():
    user = User.objects.create_superuser(
        username="mamad",
        password="amirmad2007",
        email="test@gmail.com",
        phone_number="09126809532",
    )
    return user


@pytest.fixture
def another_user_comment(another_admin, random_product):
    comment = Comment.objects.create(
        user=another_admin.profile, product=random_product, text="this is a test"
    )
    return comment


@pytest.fixture
def random_comment(admin_user, random_product):
    comment = Comment.objects.create(
        user=admin_user.profile, product=random_product, text="this is a test"
    )
    return comment


@pytest.mark.django_db
class TestCommentApi:

    def test_comment_list_response_200_status(self, api_client):
        url = reverse("comment-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_comment_list_with_normal_user_response_200_status(
        self, api_client, normal_user
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse("comment-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_comment_list_create_comment_with_normal_response_201_status(
        self, api_client, normal_user, random_product
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse("comment-list")
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_comment_list_create_comment_response_201_status(
        self, api_client, admin_user, random_product
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-list")
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_comment_with_anonymous_user_response_401_status(
        self, api_client, random_product
    ):
        url = reverse("comment-list")
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_comment_list_create_comment_response_400_status(
        self, api_client, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-list")
        data = {}
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_comment_detail_response_200_status(self, api_client, random_comment):
        url = reverse("comment-detail", kwargs={"pk": random_comment.pk})
        response = api_client.get(url)
        assert response.status_code == 200

    def test_comment_detail_response_404_status(self, api_client):
        url = reverse("comment-detail", kwargs={"pk": 1})
        response = api_client.get(url)
        assert response.status_code == 404

    def test_comment_update_response_200_status(
        self, api_client, random_comment, random_product, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-detail", kwargs={"pk": random_comment.pk})
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.put(url, data)
        print(response.data)
        assert response.status_code == 200

    def test_comment_delete_response_204_status(
        self, api_client, random_comment, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-detail", kwargs={"pk": random_comment.pk})
        response = api_client.delete(url)
        print(response.data)
        assert response.status_code == 204

    def test_comment_update_response_400_status(
        self, api_client, random_comment, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-detail", kwargs={"pk": random_comment.pk})
        data = {}
        response = api_client.put(url, data)
        assert response.status_code == 400

    def test_comment_update_response_401_status(
        self, api_client, random_comment, random_product
    ):
        url = reverse("comment-detail", kwargs={"pk": random_comment.pk})
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.put(url, data)
        assert response.status_code == 401

    def test_comment_delete_with_anonymous_response_401_status(
        self, api_client, random_comment
    ):
        url = reverse("comment-detail", kwargs={"pk": random_comment.pk})
        response = api_client.delete(url)
        assert response.status_code == 401

    def test_comment_detail_with_another_user_response_200_status(
        self, api_client, admin_user, another_user_comment
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-detail", kwargs={"pk": another_user_comment.pk})
        response = api_client.get(url)
        assert response.status_code == 200

    def test_comment_update_with_another_user_response_403_status(
        self, api_client, admin_user, another_user_comment, random_product
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-detail", kwargs={"pk": another_user_comment.pk})
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.put(url, data)
        assert response.status_code == 403

    def test_comment_delete_with_another_user_response_403_status(
        self, api_client, admin_user, another_user_comment
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse("comment-detail", kwargs={"pk": another_user_comment.pk})
        response = api_client.delete(url)
        assert response.status_code == 403

    def test_comment_detail_with_normal_user_response_200_status(
        self, api_client, normal_user, another_user_comment
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse("comment-detail", kwargs={"pk": another_user_comment.pk})
        response = api_client.get(url)
        assert response.status_code == 200

    def test_comment_update_with_normal_user_response_403_status(
        self, api_client, normal_user, another_user_comment, random_product
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse("comment-detail", kwargs={"pk": another_user_comment.pk})
        data = {"product": random_product.title, "text": "this is test"}
        response = api_client.put(url, data)
        assert response.status_code == 403

    def test_comment_delete_with_normal_user_response_403_status(
        self, api_client, normal_user, another_user_comment
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse("comment-detail", kwargs={"pk": another_user_comment.pk})
        response = api_client.delete(url)
        assert response.status_code == 403
