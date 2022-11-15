from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name