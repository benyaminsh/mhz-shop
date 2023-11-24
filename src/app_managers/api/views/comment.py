from django.utils.translation import gettext as _
from rest_framework import (
    generics,
    exceptions,
    response,
    status
)

from app_managers.api.serializers.comment import CommentSerializers

from app_products.models import CommentModel

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.base_errors import BaseErrors
from utils.permissions import IsAdminUser


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializers
    versioning_class = BaseVersioning
    permission_classes = [IsAdminUser]
    pagination_class = BasePagination
    queryset = CommentModel.objects.all()


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['OPTIONS', 'PUT', 'DELETE']
    versioning_class = BaseVersioning
    permission_classes = [IsAdminUser]
    serializer_class = CommentSerializers
    queryset = CommentModel.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        pk_param_value = self.request.GET.get(self.lookup_field, None)
        if pk_param_value is None or pk_param_value == '':
            raise exceptions.ParseError(BaseErrors._change_error_variable('parameter_is_required', param_name='pk'))
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(pk=pk_param_value).first()
        if obj is None:
            raise exceptions.NotFound(BaseErrors._change_error_variable('object_not_found', object=_('Comment')))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_pk = instance.pk
        instance_body = instance.body
        instance.delete()
        return response.Response({
            "id": instance_pk,
            "body": instance_body,
        },
            status=status.HTTP_200_OK
        )
