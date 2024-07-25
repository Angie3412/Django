#Se importa el módulo admin desde django.contrib. Este módulo proporciona funcionalidades para registrar modelos en la interfaz de administración de Django, lo que posibilita la gestión de datos a través de un panel administrativo.
from django.contrib import admin

#Se importa el modelo Programmer desde el archivo models.py en el mismo paquete. Esta acción permite que el modelo Programmer sea registrado en el panel de administración.
from .models import Programmer

#Se registra el modelo Programmer en la interfaz de administración de Django. Al registrar el modelo, se crea una interfaz en el panel de administración que permite a los usuarios gestionar instancias del modelo Programmer (crear, editar, eliminar, etc.).
admin.site.register(Programmer)