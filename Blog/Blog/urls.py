from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('cadmin.urls')),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    path('post/', include('post.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
