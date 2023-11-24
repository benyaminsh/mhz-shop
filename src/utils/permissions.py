from rest_framework.permissions import (
    AllowAny as AllowAnyPermission,
    IsAuthenticated as IsAuthenticatedPermission,
    IsAdminUser
)
from rest_framework.permissions import BasePermission




class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST', 'DELETE', 'PUT')
        return bool(request.user.is_authenticated and request.user and request.user.work_type == 'customer')


