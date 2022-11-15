from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.register_view, name='sign_up'),
    path('', views.home_view, name='home'),
]
