from rest_framework import generics

from app_products.api.serializers.comment import CommentSerializers

from app_products.models import CommentModel

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class ProductCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializers
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    queryset = CommentModel.objects.all()
