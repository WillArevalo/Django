from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas
from django.views.generic import TemplateView
# Create your views here.
class ContinentsView(TemplateView):
	template_name = "continents/continenthome.html"