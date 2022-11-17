from django.urls import path, include

urlpatterns = [
    path('category/', include('category.urls')),
    path('tag/', include('tag.urls')),
]
