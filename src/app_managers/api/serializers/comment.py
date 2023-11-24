from rest_framework import serializers
from app_products.models import CommentModel


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = (
            'id',
            'full_name',
            'email',
            'body',
            'status',
            'created',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'full_name': {'read_only': True},
            'email': {'read_only': True},
            'body': {'read_only': True},
            'status': {'required': True},
            'created': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):
        super(CommentSerializers, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT']:
                for field_name, field in self.fields.items():
                    field.required = False

        def create(self, validated_data):
            comment = CommentModel.objects.create(
                **validated_data
            )
            return comment

        def update(self, instance, validated_data):
            for field_name in validated_data:
                setattr(instance, field_name, validated_data[field_name])
            instance.save()
            return instance
