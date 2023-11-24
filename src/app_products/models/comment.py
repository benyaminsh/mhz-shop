from django.db import models
from app_products.models import ProductModel
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()


def validate_iranian_phone_number(value):
    if not value.startswith("0"):
        raise ValidationError("شماره تلفن باید با صفر شروع شود.")
    if not value.isdigit():
        raise ValidationError("شماره تلفن باید شامل اعداد باشد.")
    if len(value) != 11:
        raise ValidationError("شماره تلفن باید 11 رقمی باشد.")


class Comment(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pcomments')
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ucomments')
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=11, blank=True, null=True, validators=[validate_iranian_phone_number])
    email = models.EmailField()
    body = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} Comment {self.body[:30]}"
