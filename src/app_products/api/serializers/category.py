from rest_framework import serializers
from app_products.models import CategoryModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = (
            'id',
            'title'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'required': True},
        }
