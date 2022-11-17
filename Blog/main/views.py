from django.shortcuts import render, redirect
from .forms import RegisterForm
from post.models import Post
from django.contrib.auth import logout
from category.models import Category
from django.conf import settings
from django.contrib.auth.models import Group
def _check_groups():
    for g in settings.GROUPS:
        group = Group.objects.filter(name=g['NAME'])
        if not group:
            group = Group(name=g['NAME'])
            group.save()
def _register_post(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        _check_groups()
        group = Group.objects.get(name='default')
        user.save()
        group.user_set.add(user)
        return redirect('/')
    return render(request, 'registration/register.html', {'form': form})


def _register_get(request):
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        return _register_post(request)
    return _register_get(request)


def home_view(request):
    posts = Post.get_all(request.user)
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})


def log_out(request):
    logout(request)
    return redirect('/')
