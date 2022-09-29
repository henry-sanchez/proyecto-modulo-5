from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = "__all__" # se puede definir que campos se usaran