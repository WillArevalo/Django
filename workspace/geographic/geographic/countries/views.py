from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas
from django.views.generic import TemplateView
# Create your views here.
# definimos una funcion para que de devuelva una respuesta HTTP
class HomeView(TemplateView):
	template_name = 'countries/home.html'
	#forma de pasar inforacion a traves de los templatesviews
	def get_context_data(self, *args, **kwargs):
		colombia = {'name': 'colombia', 'code':'CO'}
		usa = {'name': 'estados unidos', 'code':'USA'}
		mexico = {'name': 'mexico', 'code': 'MX'}
		countries = [colombia, usa, mexico]
		return {'countries': countries}

