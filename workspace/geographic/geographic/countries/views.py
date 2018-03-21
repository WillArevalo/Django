from django.shortcuts import render, get_object_or_404
#renderizamos con el render
#importamos respuesta y 404
from django.http import HttpResponse, Http404
#importamos las vistas de ListView
from django.views.generic.list import ListView
#importamos el modelo Country
from countries.models import Country
from continents.models import Continent
#importamos las vistas de TemplateView
from django.views.generic import TemplateView
#importamos la vista con 404 incluida
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from countries.forms import CountryCreateFormModel

# Create your views here.

class HomeView(TemplateView):
	template_name = 'countries/home.html'

class CountryDetailView(TemplateView):
	"""docstring for CountrieView"""
	template_name = 'countries/country_detail.html'

	def get_context_data(self, *args, **kwargs):
		#En este caso el que esta recibiendo el code es el kwargs
		code = kwargs['code']
		return {'code' : code }
#Tambien hay un class Based View que hace el error 404 automatico asi:
#class CountryDetailIdView(DetailView):
#	template_name = 'countries/country_id_detail.html'
#	model = Country
#Algo que aclarar es que se debe modificar ya que llega un object y no un country el include de el template asi:
#	{% include 'countries/country.html' with country=object %}
#Tambien en la url de countries que en vez de que el parametro que se pase se llame id ahora se llame 'pk' o 'slug'
class CountryDetailIdView(TemplateView):
	"""docstring for CountrieView"""
	template_name = 'countries/country_id_detail.html'

	def get_context_data(self, *args, **kwargs):
		#Otra forma de lanzar 404 es:
		# Se le pasa modelo y query
		#country = get_object_or_404(Country,id=kwargs['id'])
		#Try por si no se encuentra country servir una pagina 404
		try:
			country = Country.objects.get(id=kwargs['id'])
		except Country.DoesNotExist as e:
			raise Http404('The Country {} does no exist'.format(kwargs['id']))
		else:
			pass
		finally:
			pass
		return {'country' : country }
		
class TagsView(TemplateView):
	template_name = 'countries/tags.html'
	
class CountrySearchView(ListView):

	template_name = 'countries/search.html'
	#Va a tomar Country va a ser un Query de todos los country y va a returnar un resultado en el template con el nombre de object_list
	model = Country

	#Funcion para filtrar
	def get_queryset(self):
		#extrayendo el parametro de la url
		query = self.kwargs['query']
		#filtro_modificado = request.POST.get('query')[:2] # obtienes los primeros 5 caracteres del parámetro query
		#Diferentes tipos de filtro 
		#name_startswith="co"
		#continent__name__contains="a"
		#Mis paises estan asociados con el continent Asia :v
		return Country.objects.filter(name__contains=query)

#Form fields = ['name','code', 'continent']

class CreateCountryView(TemplateView):
	template_name = 'countries/register.html'

	def dispatch(self, request, *args, **kwargs):
		self.form = CountryCreateFormModel(request.POST or None)
		return super().dispatch(request,*args, **kwargs)

	def get_context_data(self, *args, **kwargs):

		return {'form': self.form}

	def post(self, request, *args, **kwargs):
		
		if self.form.is_valid():
			country = self.form.save()
			return JsonResponse({
				'name': country.name,
				'code': country.code,
				'continent': str(country.continent),
				'is_active': country.active,
				})
		#Si el resultado de validar el form no es exitoso
		return self.get(request, *args, **kwargs)