from django.urls import path
from .views import badword_index, badword_create

urlpatterns = [
    path('', badword_index, name='badword_index'),
    path("create", badword_create, name="badword_create")
]
