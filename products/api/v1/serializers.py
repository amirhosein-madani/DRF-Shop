from rest_framework import serializers
from products.models.products import Product
from products.models.colors import Color
from products.models.categories import Category
from products.models.sizes import Size


class BaseSerializer(serializers.ModelSerializer):

    absolute_url = serializers.SerializerMethodField()

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())

    def to_representation(self, instance):
        """
        this is a function for overwrite fields to show
        """

        request = self.context.get("request")
        data = super().to_representation(instance)

        if request.parser_context.get("kwargs").get("pk"):
            data.pop("absolute_url", None)

        return data


class CategorySerializer(BaseSerializer):
    """
    this is a serializer for CategoryModel
    """

    class Meta:
        model = Category
        fields = ["id", "name", "absolute_url", "is_active"]


class ProductSerializer(BaseSerializer):
    """
    this is a serializer for ProductModel
    """

    color = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Color.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Category.objects.all()
    )
    size = serializers.SlugRelatedField(
        slug_field="name", many=True, queryset=Size.objects.all()
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
            "category",
            "size",
            "stock",
        ]

    def to_representation(self, instance):
        """
        this is a function for overwrite fields to show
        """

        request = self.context.get("request")
        data = super().to_representation(instance)

        if not request.parser_context.get("kwargs").get("pk"):

            data.pop("description", None)
        else:
            data.pop("absolute_url", None)

        data["category"] = CategorySerializer(
            instance.category.all(), many=True, context=self.context
        ).data

        return data


class ColorSerializer(BaseSerializer):
    """
    this is a serializer for ColorModel
    """

    class Meta:
        model = Color
        fields = ["id", "name", "absolute_url"]


class SizeSerializer(BaseSerializer):
    """
    this is a serializer for SizeModel
    """

    class Meta:
        model = Size
        fields = ["id", "name", "absolute_url"]
