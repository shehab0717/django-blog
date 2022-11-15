from django.urls import path
from . import views


urlpatterns = [
    path('create', views.category_create),
]
