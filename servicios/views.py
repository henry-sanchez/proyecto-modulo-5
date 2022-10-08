from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Usuario, Persona, Rol, Usuario, UsuarioServicio, Servicio
from .forms import PersonaForm
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import PersonaSerializer
from .serializers import ReportePersonasSerializer
from .serializers import NombrePersonaSerializer
from .serializers import RolSerializer
from .serializers import UsuarioSerializer
from .serializers import UsuarioServicioSerializer
from .serializers import ServicioSerializer

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


# para uso con rest_framework

# con generic API VIEW
class PersonaViewSet(generics.CreateAPIView, generics.ListAPIView):
  queryset = Persona.objects.all()
  serializer_class = PersonaSerializer

class RolViewSet(generics.CreateAPIView, generics.ListAPIView):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer

class UsuarioViewSet(generics.CreateAPIView, generics.ListAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class UsuarioServicioViewSet(generics.CreateAPIView, generics.ListAPIView):
  queryset = UsuarioServicio.objects.all()
  serializer_class = UsuarioServicioSerializer

class ServicioViewSet(generics.CreateAPIView, generics.ListAPIView):
  queryset = Servicio.objects.all()
  serializer_class = ServicioSerializer

# custom API
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # se restringe con autorizacion
def persona_contador(request):
  """
  Cantidad de items en el modelo persona
  """
  try:
    cantidad = Persona.objects.count()
    return JsonResponse(
      {
        "cantidad": cantidad,
      },
      safe=False,
      status=200,
    )
  except Exception as e:
      return JsonResponse(
        {
          "message": str(e)
        },
        status=400
      )

@api_view(['GET'])
def reporte_personas(request):
  """
  Reporte de personas (se serializa para representar en un JSON)
  """
  try:
    personas = Persona.objects.filter(nombre='U')
    cantidad = personas.count()
    return JsonResponse(
      ReportePersonasSerializer({
        "cantidad": cantidad,
        "personas": personas,
      }).data,
      safe=False,
      status=200,
    )
  except Exception as e:
    return JsonResponse(
      {
        "message": str(e)
      },
      status=400
    )

@api_view(['POST'])
def enviar_datos(request):
  """
  Formulario de entrada de personas (se serializa para representar en un JSON)
  """
  customSerializer = NombrePersonaSerializer(data=request.data) # indica que esta recibiendo datos de entrada
  if customSerializer.is_valid():
    return JsonResponse({"mensaje": "Datos registrados correctamente"}, status=200)
  else:
    return JsonResponse({"message": customSerializer.errors}, status=400)
