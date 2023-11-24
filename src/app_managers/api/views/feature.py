from django.utils.translation import gettext as _
from rest_framework import (
    generics,
    exceptions,
    response,
    status
)

from app_managers.api.serializers.feature import FeatureSerializers

from app_products.models import FeatureModel

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.base_errors import BaseErrors
from utils.permissions import IsAdminUser


class FeatureListCreateView(generics.ListCreateAPIView):
    serializer_class = FeatureSerializers
    versioning_class = BaseVersioning
    permission_classes = [IsAdminUser]
    pagination_class = BasePagination
    queryset = FeatureModel.objects.all()

    def get_queryset(self):
        product_id = self.request.query_params.get('productID', None)
        if product_id:
            return FeatureModel.objects.filter(product_id=product_id)
        else:
            return FeatureModel.objects.all()


class FeatureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['OPTIONS', 'PUT', 'DELETE']
    versioning_class = BaseVersioning
    permission_classes = [IsAdminUser]
    serializer_class = FeatureSerializers
    queryset = FeatureModel.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        pk_param_value = self.request.GET.get(self.lookup_field, None)
        if pk_param_value is None or pk_param_value == '':
            raise exceptions.ParseError(BaseErrors._change_error_variable('parameter_is_required', param_name='pk'))
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(pk=pk_param_value).first()
        if obj is None:
            raise exceptions.NotFound(BaseErrors._change_error_variable('object_not_found', object=_('Feature')))
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
