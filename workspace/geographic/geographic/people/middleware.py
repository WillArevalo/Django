from django.http import Http404

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
		