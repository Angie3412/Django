#Se importan los módulos path e include desde django.urls. path se utiliza para definir rutas en las URLs de Django, mientras que include se emplea para incorporar configuraciones de URL desde otros archivos.
from django.urls import path, include

#Se importa el módulo routers desde rest_framework, el cual proporciona clases para gestionar automáticamente las rutas de las vistas en una API RESTful.
from rest_framework import routers

#Se importa el módulo views desde la aplicación myapp, lo que posibilita el acceso a las vistas definidas en views.py de esa aplicación, como ProgrammerViewSet.
from myapp import views


#  Se crea una instancia de DefaultRouter, que facilita el registro de vistas y la generación automática de rutas para operaciones CRUD en una API RESTful.
router = routers.DefaultRouter()

#registra el ProgrammerViewSet con el enrutador bajo la ruta programmers. Esto implica que el enrutador generará automáticamente las rutas necesarias para manejar las solicitudes a la API relacionadas con el modelo Programmer, como listar, crear, actualizar y eliminar instancias del modelo.
router.register(r'programmers', views.ProgrammerViewSet)

#Esta línea define las URLs del archivo.
urlpatterns = [
    # Se define la configuración de URLs con path('', include(router.urls)), incluyendo todas las URLs generadas por el enrutador en la configuración principal de URLs. De esta forma, todas las rutas vinculadas al modelo Programmer se incluirán en la raíz del conjunto de URLs.
    path('', include(router.urls))
]
