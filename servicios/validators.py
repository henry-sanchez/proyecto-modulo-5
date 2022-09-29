from django.core.exceptions import ValidationError

def validar_par(value):
  if value % 2 != 0:
    raise ValidationError(
      '%(value) no es un número par%',
      params = { 'value': value },
    )

def validar_caracteres_especiales(value):
  if '@' in value:
    raise ValidationError('@ no es permitido')