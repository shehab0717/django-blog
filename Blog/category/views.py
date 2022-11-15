from django.shortcuts import render
from .forms import CategoryCreateForm


def category_create(request):
    form = CategoryCreateForm()
    return render(request, 'category/create.html', {'form': form})