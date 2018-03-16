from django.db import models

# Create your models here.
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

	