from django.shortcuts import render
#renderizamos con el render
from django.http import HttpResponse
# Create your views here.
# definimos una funcion para que de devuelva una respuesta HTTP
def home(request):
	return render(request, "countries/home.html")

