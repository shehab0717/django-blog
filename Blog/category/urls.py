from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_index, name='category_index'),
    path('index', views.category_index),
    path('create', views.category_create, name='category_create'),
    path('update/<int:id>', views.category_update, name='category_update'),
    path('delete/<int:id>', views.category_delete, name='category_delete'),
    path('details/<int:id>', views.category_details, name='category_details'),
    path('subscribe/<int:id>', views.category_toggle_subscribe, name='category_toggle_subscribe')
]
