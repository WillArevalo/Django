from countries.models import Country
#importamos nuestro modelo Country
from django.urls import reverse
#importamos el metodo para hacer reverse en las urls path
def countries_data(request):
	#Se pasa el nombre del path para crear el datail_url
	countries = Country.objects.all()
	population = 10
	return {'countries': countries, 'population': population}