from django.contrib import admin

# importacion de modelos de la aplicacion
from .models import Persona, Usuario, Servicio, UsuarioServicio, Rol

#registro de modelos para visualizar en el administrador
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Servicio)
admin.site.register(UsuarioServicio)
admin.site.register(Rol)