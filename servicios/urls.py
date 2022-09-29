from django.urls import path
from django.urls import include
# from . import views
from rest_framework.routers import DefaultRouter

# uso con rest_framework
router = DefaultRouter()
router.register('personas', views.PersonaViewSet)


urlpatterns = [
  # path('', views.index, name='index'),
  # path('categorias/', views.categoria, name='categorias'),
  # path('personas/', views.persona_form_view, name='personas'),
  
  # rest_framework
  path('', include(router.urls))
]