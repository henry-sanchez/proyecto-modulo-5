from django.contrib import admin

# importacion de modelos de la aplicacion
from .models import Persona
from .models import Usuario

#registro de modelos para visualizar en el administrador
admin.site.register(Persona)
admin.site.register(Usuario)