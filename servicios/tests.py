from django.test import TestCase
from django.test import Client
from django.test import tag
from django.core.exceptions import ValidationError
from .models import Usuario
from .models import Persona

class TestUsuario(TestCase):
  def setUp(self):
    self.client = Client()
    Persona.objects.create(nombre='Persona 1')
    Persona.objects.create(nombre='Persona 2')

  def test_grabacion_usuarios(self):
    p = Persona(nombre='persona')
    p.save()
    q = Usuario(
      user='usuario001',
      password='password',
      correo='email@correo.mail.com',
      precio_correo=20,
      persona=p
    )
    q.save()
    self.assertEqual(Usuario.objects.count(), 1)

  def test_grabacion_personas_no_permitido(self):
    q = Persona.objects.create(nombre='No permitido @')
    self.assertRaises(ValidationError, q.full_clean)
  
  @tag('validacion') # permite ejecutar solo ciertos test por su tag
  def test_grabacion_personas_no_permitido_mensaje(self):
    with self.assertRaises(ValidationError) as qv:
      q = Persona.objects.create(nombre='No permitido @')
      q.full_clean()
    
    mensaje_error = dict(qv.exception)
    self.assertEqual(mensaje_error['nombre'][0], '@ no es permitido')
  
  def test_persona_lista(self):
    response = self.client.get('/servicios/personas/')
    self.assertContains(response, 'Persona 1', status_code=200, html=True)
  
  def test_persona_filtro(self):
    response = self.client.get('/servicios/personas/?nombre=Persona 1')
    self.assertNotContains(response, 'Persona 1', status_code=200, html=True)
  
  def test_persona_formulario(self):
    response = self.client.post('/servicios/personas/', {'nombre': 'Persona 3'})
    self.assertContains(response, 'Persona 3', status_code=200, html=True)