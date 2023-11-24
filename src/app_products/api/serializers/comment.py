from rest_framework import serializers
from app_products.models import CommentModel


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = (
            'id',
            'product',
            'full_name',
            'email',
            'body',
            'status',
            'created',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'product': {'write_only': True},
            'full_name': {'required': True},
            'email': {'required': True},
            'body': {'required': True},
            'status': {'read_only': True},
            'created': {'read_only': True},
        }
