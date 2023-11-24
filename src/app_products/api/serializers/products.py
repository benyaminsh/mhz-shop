from rest_framework import serializers
from app_products.models import ProductModel
from app_products.api.serializers.category import CategorySerializers
from app_products.api.serializers.feature import FeatureSerializers
from app_products.api.serializers.comment import CommentSerializers


class ProductsSerializers(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'slug',
            'model',
            'image',
            'category',
            'created',
            'updated',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'read_only': True},
            'slug': {'read_only': True},
            'model': {'read_only': True},
            'image': {'read_only': True},
            'category': {'read_only': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
        }

    def get_category(self, obj):
        return CategorySerializers(instance=obj.category, many=False).data


class ProductInfoSerializers(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'model',
            'image',
            'category',
            'brand_en',
            'brand_fa',
            'status',
            'created',
            'updated',
            # more
            'features',
            'comments',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'read_only': True},
            'slug': {'read_only': True},
            'description': {'read_only': True},
            'model': {'read_only': True},
            'image': {'read_only': True},
            'category': {'read_only': True},
            'brand_en': {'read_only': True},
            'brand_fa': {'read_only': True},
            'status': {'read_only': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
            # more
            'features': {'read_only': True},
            'comments': {'read_only': True},
        }

    def get_category(self, obj):
        return CategorySerializers(instance=obj.category, many=False).data

    def get_features(self, obj):
        return FeatureSerializers(instance=obj.pfeatures.all(), many=True).data

    def get_comments(self, obj):
        return CommentSerializers(instance=obj.pcomments.all(), many=True).data
