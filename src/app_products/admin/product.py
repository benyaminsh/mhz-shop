from django.contrib import admin
from app_products.models import ProductModel
from .feature import FeatureAdmin


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (FeatureAdmin,)
    list_display = (
        'title',
        'slug',
        'status',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = (
        'title',
        'slug'
    )
