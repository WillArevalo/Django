from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
#importamos las vistas
from django.views.generic import View
# Create your views here.
# definimos una funcion para que de devuelva una respuesta HTTP
class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "countries/home.html")

