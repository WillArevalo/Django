from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas
from django.views.generic import TemplateView
# Create your views here.
# definimos una funcion para que de devuelva una respuesta HTTP
class HomeView(TemplateView):
	template_name = 'countries/home.html'

class TagsView(TemplateView):
	template_name = 'countries/tags.html'
	