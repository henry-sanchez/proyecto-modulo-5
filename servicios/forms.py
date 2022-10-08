from django import forms
from .models import Persona, Rol, Usuario, Servicio, UsuarioServicio

class PersonaForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = "__all__" # se puede definir que campos se usaran

class RolForm(forms.ModelForm):
  class Meta:
    model = Rol
    fields = "__all__"

class UsuarioForm(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = "__all__"

class ServicioForm(forms.ModelForm):
  class Meta:
    model = Servicio
    fields = "__all__"

class UsuarioServicioForm(forms.ModelForm):
  class Meta:
    model = UsuarioServicio
    fields = "__all__"