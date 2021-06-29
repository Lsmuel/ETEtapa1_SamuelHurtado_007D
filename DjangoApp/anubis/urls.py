from collections import namedtuple
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import formulario

urlpatterns = [
    path('', formulario, name="formulario"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)