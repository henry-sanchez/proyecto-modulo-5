from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# uso con rest_framework
router = DefaultRouter()


urlpatterns = [
  # path('', views.index, name='index'),
  # path('categorias/', views.categoria, name='categorias'),
  # path('personas/', views.persona_form_view, name='personas'),
  
  # rest_framework
  path('', include(router.urls)),
  # como api generic
  path('persona_generic/create_list', views.PersonaViewSet.as_view(), name='personas'),
  path('persona_generic/cantidad', views.persona_contador, name='contador'),
  path('usuarios_generic', views.UsuarioViewSet.as_view(), name='usuarios'),
  path('rol_generic', views.RolViewSet.as_view(), name='roles'),
  path('servicios_generic', views.ServicioViewSet.as_view(), name='servicios'),
  path('usuario_servicios_generic', views.UsuarioServicioViewSet.as_view(), name='usuario_servicios'),
  # serializador personalizado para reporte
  path('persona/reporte', views.reporte_personas, name='reporte'),
  path('registro/persona', views.enviar_datos, name='formulario_personas'),
  # autenticacion
  path('auth/', include('dj_rest_auth.urls')), # TODO: revisar
]