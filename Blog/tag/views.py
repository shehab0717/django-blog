from django.shortcuts import render, redirect
from .models import Tag
from .forms import CreateTagForm
from django.core.exceptions import ObjectDoesNotExist


def tag_create(request):
    form = CreateTagForm()
    if request.POST:
        form = CreateTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'tag/create.html', {'form': form})


def tag_index(request):
    tags = Tag.objects.all()
    return render(request, 'tag/index.html', {'tags': tags})


def tag_update(request, name):
    tag = Tag.objects.filter(name = name)
    if not tag:
        raise ObjectDoesNotExist()
    tag = tag.first()
    form = CreateTagForm()
    if request.POST:
        form = CreateTagForm( request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('/tag/index')
    return render(request, 'tag/update.html', {'form', form})

def tag_delete(request, name):
    tag = Tag.objects.filter(name = name)
    if not tag:
        raise ObjectDoesNotExist()
    tag = tag.first()
    tag.delete()
    return redirect('/tag/index')
