from django.shortcuts import render, redirect
from .forms import RegisterForm
from post.models import Post
from django.contrib.auth import logout

def _register_post(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
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
    posts = Post.get_all()
    return render(request, 'home.html', {'posts': posts})

def log_out(request):
    logout(request)
    return redirect('/')
