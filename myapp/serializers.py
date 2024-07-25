# 1.	Esta línea es adquirida  del módulo 'serializers' del paquete 'rest_framework'. 'Serializers' incluye clases y funciones para convertir ejemplos de modelos Django a diferentes formatos, como JSON, y viceversa.
from rest_framework import serializers

#Esta línea adquiere  el modelo 'Programmer' desde el archivo 'models.py' en el mismo paquete, indicado por el punto (.).
from .models import Programmer

# se define una nueva clase llamada 'ProgrammerSerializer'. Esta clase se obtiene  de 'serializers.ModelSerializer', lo que simplifica la creación de serializadores basados en modelos de Django.
class ProgrammerSerializer(serializers.ModelSerializer):

    # Dentro de 'ProgrammerSerializer', se define una clase interna llamada 'Meta' que provee metadatos sobre el serializador.
    class Meta:

        # especifica que el modelo a serializar es 'Programmer'. Al usar 'model = Programmer', se asocia el 'ProgrammerSerializer' con el modelo 'Programmer'.
        model = Programmer

        #	Esta línea indica que todos los campos del modelo 'Programmer' deben ser incluidos en el serializador. Utilizar 'fields = '_all_'' es una manera conveniente de especificar que se deben incluir todos los campos del modelo en el serializador.
        fields = '__all__'
