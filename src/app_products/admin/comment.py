from django.contrib import admin
from app_products.models import CommentModel


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'full_name',
        'status',
        'created',
    )
    list_filter = (
        'status',
    )
