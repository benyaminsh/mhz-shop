from django.db import models
from imagekit.models import ProcessedImageField
from .category import Category


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    model = models.CharField(max_length=255)
    image = ProcessedImageField(upload_to='ProductImage', options={'quality': 50})
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_en = models.CharField(max_length=255)
    brand_fa = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
