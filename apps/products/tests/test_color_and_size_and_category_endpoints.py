import pytest
from django.urls import reverse
from .test_products_endpoints import admin_user, normal_user, api_client  # noqa: F401
from products.models.sizes import Size
from products.models.colors import Color
from products.models.categories import Category


@pytest.fixture
def objects_map(db):
    color = Color.objects.create(name="test")
    size = Size.objects.create(name="test")
    category = Category.objects.create(name="test")
    return {
        "color-detail": color.pk,
        "size-detail": size.pk,
        "category-detail": category.pk,
    }


@pytest.mark.django_db
class TestColorSIzeCategoryAPI:

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-list",
            "size-list",
            "category-list",
        ],
    )
    def test_list_response_200_status(self, api_client, url_name):
        url = reverse(url_name)
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-list",
            "size-list",
            "category-list",
        ],
    )
    def test_create_with_anonymous_response_401_status(self, api_client, url_name):
        url = reverse(url_name)
        data = {"name": "test"}
        response = api_client.post(url, data)
        assert response.status_code == 401

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-list",
            "size-list",
            "category-list",
        ],
    )
    def test_create_with_normal_user_response_403_status(
        self, api_client, normal_user, url_name
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse(url_name)
        data = {"name": "test"}
        response = api_client.post(url, data)
        assert response.status_code == 403

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-list",
            "size-list",
            "category-list",
        ],
    )
    def test_create_with_admin_user_response_201_status(
        self, api_client, admin_user, url_name
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse(url_name)
        data = {"name": "test"}
        response = api_client.post(url, data)
        assert response.status_code == 201

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_detail_with_anonymous_user_response_200_status(
        self, api_client, url_name, objects_map
    ):
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        response = api_client.get(url)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_update_detail_with_normal_user_response_403_status(
        self, api_client, url_name, objects_map, normal_user
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        data = {"name": "test"}
        response = api_client.put(url, data)
        assert response.status_code == 403

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_update_detail_with_anonymous_user_response_401_status(
        self, api_client, url_name, objects_map
    ):
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        data = {"name": "test"}
        response = api_client.put(url, data)
        assert response.status_code == 401

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_update_detail_with_admin_user_response_200_status(
        self, api_client, url_name, objects_map, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        data = {"name": "test"}
        response = api_client.put(url, data)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_delete_detail_with_anonymous_user_response_401_status(
        self, api_client, url_name, objects_map
    ):
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        data = {"name": "test"}
        response = api_client.delete(url, data)
        assert response.status_code == 401

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_delete_detail_with_normal_user_response_403_status(
        self, api_client, url_name, objects_map, normal_user
    ):
        api_client.force_authenticate(user=normal_user)
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        data = {"name": "test"}
        response = api_client.delete(url, data)
        assert response.status_code == 403

    @pytest.mark.parametrize(
        "url_name",
        [
            "color-detail",
            "size-detail",
            "category-detail",
        ],
    )
    def test_delete_detail_with_admin_user_response_204_status(
        self, api_client, url_name, objects_map, admin_user
    ):
        api_client.force_authenticate(user=admin_user)
        url = reverse(url_name, kwargs={"pk": objects_map[url_name]})
        data = {"name": "test"}
        response = api_client.delete(url, data)
        assert response.status_code == 204
