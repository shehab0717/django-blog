from django.urls import path
from . import views

urlpatterns = [
    path('create', views.post_create, name='post_create'),
    path('details/<int:id>', views.post_details, name='post_details'),
    path('update/<int:id>', views.post_update, name='post_update'),
]
