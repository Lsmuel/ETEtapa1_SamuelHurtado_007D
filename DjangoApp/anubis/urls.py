from collections import namedtuple
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import formulario, VerColaboradores, modColaborador, delColaborador, actualizar

urlpatterns = [
    path('', formulario, name="formulario"),
    path('mostrar', VerColaboradores, name="mostrar" ),
    path('modColaborador/<id>', modColaborador, name="modColaborador"),
    path('delColaborador/<id>', delColaborador, name="delColaborador"),
    path('actualizar', actualizar, name='actualizar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)