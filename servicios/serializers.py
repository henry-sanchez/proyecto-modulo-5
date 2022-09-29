from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers):
  class Meta:
    model = Persona
    fields = '__all__'