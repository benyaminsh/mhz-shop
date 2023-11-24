from django.db import models
from app_products.models import ProductModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pcomments')
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ucomments')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} Comment {self.body[:30]}"
