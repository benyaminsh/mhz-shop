from rest_framework import serializers
from app_products.models import FeatureModel


class FeatureSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeatureModel
        fields = (
            'id',
            'product',
            'title',
            'description',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'product': {'required': True},
            'title': {'required': True},
            'description': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super(FeatureSerializers, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT']:
                for field_name, field in self.fields.items():
                    field.required = False

    def create(self, validated_data):
        feature = FeatureModel.objects.create(
            **validated_data
        )
        return feature

    def update(self, instance, validated_data):
        for field_name in validated_data:
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
