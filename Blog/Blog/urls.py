from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from main import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    path('category/', include('category.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
