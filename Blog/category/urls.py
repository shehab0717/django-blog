from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_index, name='categor_index'),
    path('index', views.category_index),
    path('create', views.category_create, name='categor_create'),
    path('update/<int:id>', views.category_update, name='categor_update'),
    path('delete/<int:id>', views.category_delete, name='categor_delete'),
    path('details/<int:id>', views.category_details, name='category_details'),
    path('subscribe/<int:id>', views.category_toggle_subscribe, name='category_toggle_subscribe')
]
