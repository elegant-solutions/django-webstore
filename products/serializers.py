from rest_framework import serializers
from .models import Category, Product


class ProductDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "image",
            "price",
        ]

    def get_image(self, obj):
        return obj.productimage_set.first().image.url


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product_detail_api')
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "url",
            "id",
            "title",
            "description",
            "image",
            "price",
        ]

    def get_image(self, obj):
        return obj.productimage_set.first().image.url


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
    product_set = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = [
                "url",
                "id",
                "title",
                "description",
                "product_set",
                # "default_category"
            ]
