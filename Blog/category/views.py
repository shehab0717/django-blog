from django.shortcuts import render, redirect
from .forms import CategoryCreateForm
from .models import CategoryModel


def category_create(request):
    if request.POST:
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category')
        return render(request, 'category/create.html', {'form': form})
    
    form = CategoryCreateForm()
    return render(request, 'category/create.html', {'form': form})


def category_index(request):
    categories = CategoryModel.objects.all()
    return render(request, 'category/index.html', {'categories': categories})




def category_update(request, id):
    category = CategoryModel.objects.get(pk = id)
    if request.POST:
        form = CategoryCreateForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/category')
        return render(request, 'category/index.html', {'form': form})
    form = CategoryCreateForm(instance=category)
    return render(request, 'category/update.html', {'form': form})


def category_delete(request, id):
    category = CategoryModel.objects.get(pk = id)
    if request.POST:
        category.delete()
        return redirect('/category')
    return render(request, 'category/delete.html', {'category': category})

def category_details(request, id):
    category = CategoryModel.objects.get(pk = id)
    return render(request, 'category/details.html', {'category': category})