#Se importa AppConfig desde django.apps. AppConfig es una clase base que se utiliza para configurar las opciones de una aplicación Django.
from django.apps import AppConfig

#Aquí se define una nueva clase llamada ApiConfig que hereda de AppConfig. Esta clase se utiliza para configurar la aplicación myapp.
class ApiConfig(AppConfig):

    #Esta línea especifica el tipo de campo para las claves primarias automáticas. BigAutoField es un campo que utiliza enteros grandes para las claves primarias, lo cual es útil para manejar grandes cantidades de datos. Esta configuración se aplica por defecto a los modelos que no especifican un campo de clave primaria explícitamente.
    default_auto_field = 'django.db.models.BigAutoField'

    #Esta línea define el nombre de la aplicación como myapp. Este nombre debe coincidir con el nombre del directorio de la aplicación y se utiliza para hacer referencia a la aplicación dentro del proyecto Django.
    name = 'myapp'
