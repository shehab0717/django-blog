from django.shortcuts import render, redirect
from .forms import CategoryCreateForm
from .models import CategoryModel


def _category_create_post(request):
    form = CategoryCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/category')
    return render(request, 'category/create.html', {'form': form})


def category_create(request):
    if request.POST:
        return _category_create_post(request)
    
    form = CategoryCreateForm()
    return render(request, 'category/create.html', {'form': form})


def category_index(request):
    categories = CategoryModel.objects.all()
    return render(request, 'category/index.html', {'categories': categories})