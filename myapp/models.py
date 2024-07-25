
# Esta línea importa el módulo 'models' desde el paquete 'django.db', el cual incluye las clases y funciones para definir modelos de base de datos en Django.
from django.db import models 

# se define una nueva clase llamada 'Programmer'. Esta clase se obtiene de 'models.Model', lo cual indica que será un modelo en Django que se asociará a una tabla en la base de datos.
class Programmer(models.Model):

# se establece un campo llamado 'reference' de tipo texto utilizando 'models.CharField'. Este tipo de campo permite almacenar cadenas de texto de longitud variable hasta un máximo de 100 caracteres, especificado por 'max_length=100'.
    reference = models.CharField(max_length=100)

# se define un campo de texto llamado 'trademark' de manera similar al campo 'reference'. Este campo también puede almacenar hasta 100 caracteres de longitud.
    trademark = models.CharField(max_length=100)

 # se define un nuevo campo de texto llamado 'pattern', el cual tiene un límite de 100 caracteres para su almacenamiento.
    pattern = models.CharField(max_length=100)

# se define un campo numérico llamado 'price' que almacenará valores enteros. Se utiliza 'models.IntegerField' para representar valores numéricos enteros sin decimales.
    price = models.IntegerField()
    
 # se define un campo de texto llamado 'supplier' con un límite máximo de 100 caracteres. Este campo podría utilizarse para almacenar el nombre del proveedor del programador.
    supplier = models.CharField(max_length=100)
