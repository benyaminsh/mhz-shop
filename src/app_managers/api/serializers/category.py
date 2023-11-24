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

    def __init__(self, *args, **kwargs):
        super(CategorySerializers, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT']:
                for field_name, field in self.fields.items():
                    field.required = False

    def create(self, validated_data):
        category = CategoryModel.objects.create(
            **validated_data
        )
        return category

    def update(self, instance, validated_data):
        for field_name in validated_data:
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
