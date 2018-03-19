from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from continents.models import Continent
from countries.models import Country
# Create your views here.
class ContinentsView(TemplateView):
	template_name = "continents/continenthome.html"

	def get_context_data(self, *args, **kwargs):
		data = {'data':'56'}
		return {'data':data}


class ContinentDetailView(DetailView):
	template_name = "continents/continent_detail.html"
	model = Continent

