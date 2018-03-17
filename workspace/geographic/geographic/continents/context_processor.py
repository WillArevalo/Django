from continents.models import Continent
def continents_data(request):
	continents = Continent.objects.all()
	population = 10
	return {'continents': continents, 'population': population}