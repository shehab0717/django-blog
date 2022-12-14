from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.register_view, name='sign_up'),
    path('login', views.login, name='custom_login'),
    path('log-out', views.log_out, name='log_out'),
    path('', views.home_view, name='home'),
]
