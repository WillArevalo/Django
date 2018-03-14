from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas
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
	