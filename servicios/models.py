from django.db import models

class Persona(models.Model):
  nombre = models.CharField(max_length=100)

  def __str__(self):
    return self.nombre

class Usuario(models.Model):
  user = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=128)
  enviar_correo = models.BooleanField(default=False)
  precio_correo = models.DecimalField(max_digits=10, decimal_places=2)
  persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
  # persona = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Persona')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)