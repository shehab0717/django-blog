from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from post.models import Post
from django.contrib.auth import logout, authenticate, login as dlogin
from category.models import Category
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import UserStatus
from django.db.models import Q


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
        u_status = UserStatus(user=user)
        u_status.save()
        return redirect(reverse('custom_login'))
    return render(request, 'registration/register.html', {'form': form})


def _register_get(request):
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        return _register_post(request)
    return _register_get(request)


def home_view(request):
    search = request.GET['search'] if 'search' in request.GET else ''
    posts = Post.get_all(request.user, search=search)
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})


def log_out(request):
    logout(request)
    return redirect(reverse('custom_login'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                print('found user')
                if user.is_staff or not user.userstatus.is_blocked:
                    dlogin(request, user)
                    return redirect(reverse('home'))
                else:
                    form.add_error(
                        field=None, error='This user is blocked, contact the admin to help you')
    return render(request, 'registration/login.html', {'form': form})