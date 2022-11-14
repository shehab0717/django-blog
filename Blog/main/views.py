from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def RegisterView(request):
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# def Index(request):
#     return render(request, 'regi')