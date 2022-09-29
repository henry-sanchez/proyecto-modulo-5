from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .models import Persona
from .forms import PersonaForm

def index(request):
  return HttpResponse('Hola Mundo')

def categoria(request):
  post_nombre = request.POST.get('nombre')
  if post_nombre:
    q = Usuario(nombre=post_nombre)
    q.save()
  
  filtro_nombre = request.GET.get('nombre')
  #if filtro_nombre:
  #  usuarios = Usuario.objects.filter()

# trabajando con model forms
def persona_form_view(request):
  form = PersonaForm(request.POST) # todo el form que viene en el POST se envia al formulario
  persona = None
  # validando si no existe un determinado item
  id_persona = request.GET.get('id')
  if id_persona:
    # persona = Persona.objects.filter(id=id_persona)
    persona = get_object_or_404(Persona, id=id_persona)
    form = PersonaForm(instance=persona)
  
  if request.method == 'POST':
    if persona:
      form = PersonaForm(request.POST, instance=persona)
    else:
      form = PersonaForm((request.POST))

  if form.is_valid():
    form.save()
  return render(request, 'form_personas.html', {"form": form })