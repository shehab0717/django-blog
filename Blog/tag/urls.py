from django.urls import path
from . import views

urlpatterns = [
    path('index', views.tag_index, name='tag_index'),
    path('create', views.tag_create, name='tag_create'),
    path('update/<str:name>', views.tag_update, name='tag_update'),
    path('delete/<str:name>', views.tag_delete, name='tag_delete'),
]
