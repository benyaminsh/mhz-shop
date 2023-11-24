from django.db import models
from app_products.models import ProductModel


class Feature(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pfeatures')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
