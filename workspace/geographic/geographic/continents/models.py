from django.db import models

# Create your models here.
class Continent(models.Model):
	name = models.CharField(max_length=200)
	translate = models.CharField(max_length=200)
	color = models.CharField(max_length=200)

	#funcion para mostrar el nombre del objeto en vez de un nombre generico
	def __str__(self):
		return self.name