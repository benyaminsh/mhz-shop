from django.utils.translation import gettext as _
from rest_framework import generics, exceptions

from app_products.api.serializers.products import (
    ProductsSerializers,
    ProductInfoSerializers
)

from app_products.models import ProductModel

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.base_errors import BaseErrors


class ProductsView(generics.ListAPIView):
    serializer_class = ProductsSerializers
    versioning_class = BaseVersioning
    pagination_class = BasePagination

    def get_queryset(self):
        return ProductModel.objects.filter(status=True).all()


class ProductRetrieveView(generics.RetrieveAPIView):
    allowed_methods = ['OPTIONS']
    versioning_class = BaseVersioning
    serializer_class = ProductInfoSerializers
    queryset = ProductModel.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        pk_param_value = self.request.GET.get(self.lookup_field, None)
        if pk_param_value is None or pk_param_value == '':
            raise exceptions.ParseError(BaseErrors._change_error_variable('parameter_is_required', param_name='pk'))
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(pk=pk_param_value, status=True).first()
        if obj is None:
            raise exceptions.NotFound(BaseErrors._change_error_variable('object_not_found', object=_('Product')))
        return obj
