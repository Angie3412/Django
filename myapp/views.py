# Se importa el módulo viewsets de rest_framework, que simplifica la creación de vistas para operaciones CRUD en modelos de Django.
from rest_framework import viewsets

#Se importa el modelo Programmer desde models.py en el mismo paquete, permitiendo que el ProgrammerViewSet trabaje con este modelo.
from .models import Programmer

#Se importa el serializador ProgrammerSerializer desde serializers.py en el mismo paquete, para que el ProgrammerViewSet pueda convertir datos del modelo a formatos como JSON.
from .serializers import ProgrammerSerializer


#Se crea una nueva clase llamada ProgrammerViewSet, que hereda de viewsets.ModelViewSet para manejar operaciones CRUD en un modelo.
class ProgrammerViewSet(viewsets.ModelViewSet):

#Se establece que el queryset para recuperar instancias del modelo Programmer es Programmer.objects.all(), que devuelve todas las instancias del modelo en la base de datos.
    queryset = Programmer.objects.all()

#Se especifica que se usará el serializador ProgrammerSerializer para convertir instancias del modelo Programmer a JSON y viceversa, indicando qué clase de serializador se utilizará para la serialización y deserialización de datos.
    serializer_class = ProgrammerSerializer
