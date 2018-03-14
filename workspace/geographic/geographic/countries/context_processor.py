from django.urls import reverse
#importamos el metodo para hacer reverse en las urls path
def countries_data(request):
	#Se pasa el nombre del path para crear el datail_url
	colombia = {
	'name': 'colombia', 'code':'CO', 'id': 1,
	'detail_url': reverse("country_id_detail", kwargs={'id':1})
	}
	usa = {
	'name': 'estados unidos', 'code':'USA', 'id': 2,
	'detail_url': reverse("country_id_detail", kwargs={'id':2})
	}
	mexico = {
	'name': 'mexico', 'code': 'MX', 'id': 3,
	'detail_url': reverse("country_id_detail", kwargs={'id':3})
	}
	countries = [colombia, usa, mexico]
	population = 10
	return {'countries': countries, 'population': population}