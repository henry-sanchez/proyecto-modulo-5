from django.core.exceptions import ValidationError

def validar_par(value):
  if value % 2 != 0:
    raise ValidationError(
      '%(value) no es un número par%',
      params = { 'value': value },
    )

def precio_maximo(value):
  if value > 1000:
    raise ValidationError(
      '%Precio no puede superar 1000 Bs%',
    )

def validar_caracteres_especiales(value):
  if '@' in value:
    raise ValidationError('@ no es permitido')

# custom serializer para input
def validar_nombre_subject(value):
  if value == 'Comida':
    raise ValidationError('Comida no es permitido')