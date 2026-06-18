from rest_framework import serializers
from reviews.models import Comment
from products.models.products import Product


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    product = serializers.SlugRelatedField(
        slug_field="title", queryset=Product.objects.all()
    )
    absolute_url = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "user",
            "product",
            "text",
            "created_at",
            "absolute_url",
            "is_active",
            "reply",
        ]

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

        else:

            data.pop("text", None)

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user.profile
        return super().create(validated_data)
