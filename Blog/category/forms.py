from django.forms import ModelForm
from .models import CategoryModel

class CategoryCreateForm(ModelForm):
    class Meta:
        model = CategoryModel
        fields = ["name"]