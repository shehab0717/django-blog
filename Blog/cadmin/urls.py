from django.urls import path, include
from .views import admin_index, post_index, user_index, make_admin

urlpatterns = [
    path('', admin_index, name="admin_index"),
    path('post/index', post_index, name="post_index"),
    path('user/index', user_index, name="user_index"),
    path('user/make-admin/<int:id>', make_admin, name="make_admin"),
    path('category/', include('category.urls')),
    path('tag/', include('tag.urls')),
]
