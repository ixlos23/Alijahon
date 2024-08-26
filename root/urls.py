from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.views import CustomLoginView
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('login', CustomLoginView.as_view(), name='login'),
    path('', include('apps.urls')),
]
