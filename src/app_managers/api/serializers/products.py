from django.utils.text import slugify
from rest_framework import serializers
from app_products.models import ProductModel
from app_products.api.serializers.category import CategorySerializers
from app_products.api.serializers.feature import FeatureSerializers
from app_products.api.serializers.comment import CommentSerializers


class ProductsSerializers(serializers.ModelSerializer):
    category_info = serializers.SerializerMethodField()
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
            'category_info',
            'features',
            'comments',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'required': True},
            'slug': {'read_only': True},
            'description': {'required': True},
            'model': {'required': True},
            'image': {'required': True},
            'category': {'write_only': True},
            'brand_en': {'required': True},
            'brand_fa': {'required': True},
            'status': {'required': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
            # more
            'category_info': {'read_only': True},
            'features': {'read_only': True},
            'comments': {'read_only': True},
        }

    def get_category_info(self, obj):
        return CategorySerializers(instance=obj.category, many=False).data

    def get_features(self, obj):
        return FeatureSerializers(instance=obj.pfeatures.all(), many=True).data

    def get_comments(self, obj):
        return CommentSerializers(instance=obj.pcomments.all(), many=True).data

    def __init__(self, *args, **kwargs):
        super(ProductsSerializers, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT']:
                for field_name, field in self.fields.items():
                    field.required = False

    def create(self, validated_data):
        product = ProductModel.objects.create(
            slug=slugify(validated_data['title'][:30]),
            **validated_data
        )
        return product

    def update(self, instance, validated_data):
        for field_name in validated_data:
            if field_name == 'title':
                setattr(instance, field_name, validated_data[field_name])
                setattr(instance, 'slug', slugify(instance.title[:30]))
            else:
                setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
