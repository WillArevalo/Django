from django.db import models

# Create your models here.
class Continent(models.Model):
	name = models.CharField(max_length=200)
	translate = models.CharField(max_length=200)
	color = models.CharField(max_length=200)
