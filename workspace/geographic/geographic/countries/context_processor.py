def countries_data(request):
	colombia = {'name': 'colombia', 'code':'CO'}
	usa = {'name': 'estados unidos', 'code':'USA'}
	mexico = {'name': 'mexico', 'code': 'MX'}
	countries = [colombia, usa, mexico]
	population = 10
	return {'countries': countries, 'population': population}