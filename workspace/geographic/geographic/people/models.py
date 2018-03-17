from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=200)
	#relacion Muchos a Muchos.
	nacionality = models.ManyToManyField('countries.Country')
	#relacion uno a uno con el padre de la persona que se llama a si misma con self
	father = models.OneToOneField('self',on_delete=models.CASCADE,null=True)
	#Por lo tanto con el null=TRUE si una persona se crea no va a ser obligatorio que rellene el campo father
