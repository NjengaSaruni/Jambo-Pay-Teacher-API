from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('rest.urls', namespace='api')),
    url(r'^adminss/', admin.site.urls),
    url(r'^browsable/', include(
      'rest_framework.urls', namespace='rest_framework')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
