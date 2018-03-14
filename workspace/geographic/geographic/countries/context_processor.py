def countries_data(request):
	colombia = {'name': 'colombia', 'code':'CO', 'id': 1}
	usa = {'name': 'estados unidos', 'code':'USA', 'id': 2}
	mexico = {'name': 'mexico', 'code': 'MX', 'id': 3}
	countries = [colombia, usa, mexico]
	population = 10
	return {'countries': countries, 'population': population}