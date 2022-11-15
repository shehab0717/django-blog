from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)