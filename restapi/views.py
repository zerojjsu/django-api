from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HomeworkSerializer
from .models import Homework

# Serializador de API
class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all().order_by('id')
    serializer_class = HomeworkSerializer

# Mandar modelo a index
def index(request):
    tareas = Homework.objects.all()
    return render(request, 'index.html', {"tareas": tareas})
    
# Función para agregar tareas 
def agregarTarea(request):
    tarea = request.POST["tarea"]
    descripcion = request.POST["descripcion"]
    asignatura = request.POST["asignatura"]
    fecha = request.POST["fecha"]
    nivel = int(request.POST["nivel"])

    nuevo = Homework.objects.create(
        tarea = tarea,
        descripcion = descripcion,
        asignatura = asignatura,
        fecha_entrega = fecha,
        nivel = nivel,
    )
    return render(request, 'result.html', {"tarea": tarea, "fecha" : fecha})

