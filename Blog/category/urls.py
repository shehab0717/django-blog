from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_index),
    path('index', views.category_index),
    path('create', views.category_create),
    path('update/<int:id>', views.category_update),
    path('delete/<int:id>', views.category_delete),
    path('details/<int:id>', views.category_details),
]
