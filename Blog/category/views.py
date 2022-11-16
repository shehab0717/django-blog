from django.shortcuts import render, redirect
from .forms import CategoryCreateForm
from .models import Category


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
    categories = Category.objects.all()
    if request.POST: #subscribe to a category
        category_id = request.POST['category_id']
        category = Category.objects.get(pk = category_id)
        category.toggle_subscribe(request.user)
    return render(request, 'category/index.html', {'categories': categories})




def category_update(request, id):
    category = Category.objects.get(pk = id)
    if request.POST:
        form = CategoryCreateForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/category')
        return render(request, 'category/index.html', {'form': form})
    form = CategoryCreateForm(instance=category)
    return render(request, 'category/update.html', {'form': form})


def category_delete(request, id):
    category = Category.objects.get(pk = id)
    if request.POST:
        category.delete()
        return redirect('/category')
    return render(request, 'category/delete.html', {'category': category})

def category_details(request, id):
    category = Category.objects.get(pk = id)
    return render(request, 'category/details.html', {'category': category})


def category_toggle_subscribe(request, id):
    if request.POST:
        category = Category.objects.get(pk = id)
        category.toggle_subscribe(request.user)
        return redirect('/')
    return render(request, 'shared/not_found.html')

    
    