from django.db import models

# Create your models here.

#Creamos un Custom Manager
class ActiveManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(active=True)

# Este modelo representara un pais dentro de nuestra base de datos
class Country(models.Model):

	CODES_CHOICES = (
		('colombia', 'CO'),
		('mexico', 'MX'),
		('estados unidos', 'USA'),
		('argentina', 'AR'),
	)
	#Los modelos internamente tienen un id autoincremental
	#Campo de tipo char que necesita el maximo de longitud de la cadena
	name = models.CharField(max_length=255)
	#Si queremos limitar a una cierta tipa de opcione que utilice los codigos de arriba
	code = models.CharField(max_length=3, choices=CODES_CHOICES)
	#Genero un nuevo campo para hacer la relacione entre continents y countries
	continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)
	#Borrado en modo casacada para que cuando se borre un continent se borren todos los paises asociados
	active = models.BooleanField(default=True)
	#Active es un campo que si sirve para mostrar o no mostrar un campo
	active_manager = ActiveManager()
	#active_manager para filtrar y solo mostrar los que debemos
	objects = models.Manager()
	#Nuestro objects por defecto desaparece asi que los volvemos a instanciar

	#funcion para mostrar el nombre del objeto en vez de un nombre generico
	def __str__(self):
		return self.name