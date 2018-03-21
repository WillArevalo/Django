from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=200)
	#relacion Muchos a Muchos.
	nacionality = models.ManyToManyField('countries.Country')
	#relacion uno a uno con el padre de la persona que se llama a si misma con self
	father = models.OneToOneField('self',on_delete=models.CASCADE,blank=True,null=True,related_name='children')#blank=true a nivel formulario, null=true a nivel model
	#Por lo tanto con el null=TRUE si una persona se crea no va a ser obligatorio que rellene el campo father
	# El modelFrom determina si un campo es obligatorio por el atributo blank en el modelo, mas no el atributo null
	# Establece una relación contraria de padre a hijo
    # que nos permitirá saber si ya tiene un hijo asignado.
	
	#funcion para mostrar el nombre del objeto en vez de un nombre generico
	def __str__(self):
		return self.first_name