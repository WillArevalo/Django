from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas de ListView
from django.views.generic.list import ListView
#importamos el modelo Country
from countries.models import Country
#importamos las vistas de TemplateView
from django.views.generic import TemplateView
# Create your views here.
# definimos una funcion para que de devuelva una respuesta HTTP
class HomeView(TemplateView):
	template_name = 'countries/home.html'

class CountryDetailView(TemplateView):
	"""docstring for CountrieView"""
	template_name = 'countries/country_detail.html'

	def get_context_data(self, *args, **kwargs):
		#En este caso el que esta recibiendo el code es el kwargs
		code = kwargs['code']
		return {'code' : code }

class CountryDetailIdView(TemplateView):
	"""docstring for CountrieView"""
	template_name = 'countries/country_id_detail.html'

	def get_context_data(self, *args, **kwargs):
		#En este caso el que esta recibiendo el code es el args
		idCode = kwargs['id']
		return {'idCode' : idCode }
		
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
