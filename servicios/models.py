from django.db import models

class Cliente(models.Model):
  nombre = models.CharField(max_length=100)
  