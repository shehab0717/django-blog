from django.urls import path
from .views import badword_index, badword_create, badword_delete

urlpatterns = [
    path('', badword_index, name='badword_index'),
    path("create", badword_create, name="badword_create"),
    path("create/<int:id>", badword_delete, name="badword_delete")
]
