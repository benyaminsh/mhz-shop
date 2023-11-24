from django.contrib import admin
from app_products.models import FeatureModel


class FeatureAdmin(admin.StackedInline):
    model = FeatureModel
    can_delete = True
