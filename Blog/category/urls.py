from django.urls import path
from . import views


urlpatterns = [
    path('create', views.category_create),
    path('', views.category_index),
    path('index', views.category_index),
]
