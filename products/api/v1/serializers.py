from rest_framework import serializers
from products.models.products import Product
from products.models.colors import Color
from products.models.categories import Category
from products.models.sizes import Size


class CategorySerializer(serializers.ModelSerializer):
    """
    this is a serializer for CategoryModel
    """

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "absolute_url", "is_active"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())


class ProductSerializer(serializers.ModelSerializer):
    """
    this is a serializer for ProductModel
    """

    absolute_url = serializers.SerializerMethodField()
    color = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Color.objects.all()
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "absolute_url",
            "price",
            "color",
            "size",
            "stock",
        ]

    def get_absolute_url(self, obj):

        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())


class ColorSerializer(serializers.ModelSerializer):
    """
    this is a serializer for ColorModel
    """

    class Meta:
        model = Color
        fields = [
            "name",
        ]


class SizeSerializer(serializers.ModelSerializer):
    """
    this is a serializer for SizeModel
    """

    class Meta:
        model = Size
        fields = [
            "name",
        ]
