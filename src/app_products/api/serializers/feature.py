from rest_framework import serializers
from app_products.models import FeatureModel


class FeatureSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeatureModel
        fields = (
            'id',
            'title',
            'description',
        )
