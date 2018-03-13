def continents_data(request):
	america = {'name': 'america', 'translate':'america', 'color':'green'}
	africa = {'name': 'africa', 'translate':'africa', 'color':'yellow'}
	europa = {'name': 'europa', 'translate': 'europe', 'color':'red'}
	antartida = {'name': 'antartida', 'translate': 'antarctica', 'color':'blue'}
	australia = {'name': 'australia', 'translate': 'australia', 'color':'purple'}
	asia = {'name': 'asia', 'translate': 'asia', 'color':'orange'}
	continents = [america, africa, europa, antartida, australia, asia,]
	population = 10
	return {'continents': continents, 'population': population}