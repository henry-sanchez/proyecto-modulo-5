from rest_framework import serializers
from .models import Persona, Rol, Usuario, UsuarioServicio, Servicio
from .validators import validar_nombre_subject

class PersonaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persona
    fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rol
    fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = '__all__'

class UsuarioServicioSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsuarioServicio
    fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Servicio
    fields = '__all__'


## personalizado (similar a construir un modelo, para definir un esquema de validacion)
class ReportePersonasSerializer(serializers.Serializer):
  cantidad = serializers.IntegerField()
  personas = PersonaSerializer(many=True)

# similar a esquema de validacion de input
# TODO: revisar atributo max_length
class NombrePersonaSerializer(serializers.Serializer):
  nombre = serializers.CharField(
    max_length=100,
    validators=[validar_nombre_subject],
  ) # se definen para cada campo deseado
  personas = PersonaSerializer(many=True)