from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title
