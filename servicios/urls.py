from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# uso con rest_framework
router = DefaultRouter()
router.register('personas', views.PersonaViewSet)


urlpatterns = [
  # path('', views.index, name='index'),
  # path('categorias/', views.categoria, name='categorias'),
  # path('personas/', views.persona_form_view, name='personas'),
  
  # rest_framework
  path('', include(router.urls)),
  # como api generic
  path('persona_generic/create_list', views.PersonaViewSet_2.as_view(), name='personas'),
  path('persona_generic/cantidad', views.persona_contador, name='contador'),
  # serializador personalizado para reporte
  path('persona/reporte', views.reporte_personas, name='reporte'),
  # path('registro/persona', views.enviar_datos, name='formulario_personas')
  # autenticacion
  path('auth/', include('dj_rest_auth.urls')), # TODO: revisar
]