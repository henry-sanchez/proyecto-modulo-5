from django.db import models
from .validators import validar_par, validar_caracteres_especiales, precio_maximo
from django.core.validators import EmailValidator

class Persona(models.Model):
  nombre = models.CharField(max_length=100, validators=[validar_caracteres_especiales])
  telefono = models.CharField(max_length=20, null=True)
  direccion = models.CharField(max_length=50, null=True)
  fecha_nacimiento = models.DateField(null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nombre

class TipoServicio(models.TextChoices):
  CORREO = 'C', 'Correo'
  SMS = 'S', 'Sms'
  WHATSAPP = 'W', 'Whatsapp'
  TWITTER = 'T', 'Twitter'
  FACEBOOK = 'F', 'Facebook'

class Rol(models.Model):
  rol = models.CharField(max_length=15)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.rol

class Usuario(models.Model):
  user = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=128)
  correo = models.EmailField(validators=[EmailValidator('No es un email válido')])
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
  rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

  def __str__(self):
    return self.user

class Servicio(models.Model):
  nombre = models.CharField(max_length=20)
  tipo = models.CharField(
    max_length=1,
    choices=TipoServicio.choices,
    default=TipoServicio.CORREO
  )
  precio = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[precio_maximo], # se puede definir mas de una validacion
  )
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nombre

class UsuarioServicio(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
  limite = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.usuario+self.servicio

# si se requiere usar nombres convencionales de tablas
# class Meta:
  # managed = False
  #db_table = 'servicios'