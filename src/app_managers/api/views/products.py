from django.utils.translation import gettext as _
from rest_framework import (
    generics,
    exceptions,
    response,
    status
)

from app_managers.api.serializers.products import ProductsSerializers

from app_products.models import ProductModel

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.base_errors import BaseErrors
from utils.permissions import IsAdminUser


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductsSerializers
    versioning_class = BaseVersioning
    permission_classes = [IsAdminUser]
    pagination_class = BasePagination
    queryset = ProductModel.objects.all()


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['OPTIONS', 'PUT', 'DELETE']
    versioning_class = BaseVersioning
    permission_classes = [IsAdminUser]
    serializer_class = ProductsSerializers
    queryset = ProductModel.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        pk_param_value = self.request.GET.get(self.lookup_field, None)
        if pk_param_value is None or pk_param_value == '':
            raise exceptions.ParseError(BaseErrors._change_error_variable('parameter_is_required', param_name='pk'))
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(pk=pk_param_value).first()
        if obj is None:
            raise exceptions.NotFound(BaseErrors._change_error_variable('object_not_found', object=_('Product')))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_pk = instance.pk
        instance_title = instance.title
        instance.delete()
        return response.Response({
            "id": instance_pk,
            "title": instance_title,
        },
            status=status.HTTP_200_OK
        )
