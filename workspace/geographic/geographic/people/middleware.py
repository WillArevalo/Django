from django.http import Http404
#para generar aletoriedad al momento de asignar en el testab
import random

class SecretMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		#Esto se ejecuta antes de la vista
		# Si esta variable existe en la url entonces
		if not request.GET.get('secret'):
			raise Http404()
		if request.GET.get('secret') != 'platzi':
			raise Http404()
		#Entonces si intentamos entrar a la ruta normal no arrojara 404
		# si entramos con '?secret=platzi' ya servira
		response = self.get_response(request)
		#Todo lo que esta aca de ejecuta despues de la vista
		return response

class ABMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		#Esto se ejecuta antes de la vista
		#session es una variable que se guarda mientras se tenga una sesion activa
		#durante el tiempo que se este en la pagina se mantendra la misma sesion,
		#cuando se cierra el navegador se cierra la sesion, 
		# tambien se crea una nueva session cada vez que se logea, se puede utilizar como un dict
		if 'testab' not in request.session:
			request.session['testab'] = random.choice(['a','b'])
			
		response = self.get_response(request)
		#Todo lo que esta aca de ejecuta despues de la vista
		return response
