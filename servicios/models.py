from django.db import models
from .validators import validar_par
from .validators import validar_caracteres_especiales
from django.core.validators import EmailValidator

class Persona(models.Model):
  nombre = models.CharField(max_length=100, validators=[validar_caracteres_especiales])

  def __str__(self):
    return self.nombre
class Tipos(models.TextChoices):
  UNITS = 'u', 'Unidades'
  KG = 'kg', 'Kilogramos'
class Usuario(models.Model):
  user = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=128)
  correo = models.EmailField(validators=[EmailValidator('No es un email válido')])
  enviar_correo = models.BooleanField(default=False)
  precio_correo = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[validar_par], # se puede definir mas de una validacion
  )
  persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
  # persona = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Persona')
  unidades = models.CharField(
    max_length=2,
    choices=Tipos.choices,
    default=Tipos.UNITS
  )
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

# si se requiere usar nombres convencionales de tablas
# class Meta:
  # managed = False
  #db_table = 'servicios'