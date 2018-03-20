from django.shortcuts import render
from django.http import JsonResponse
from people.forms import RegisterForm
from people.models import Person

# Create your views here.
def register(request):
	#mandando request.POST podemos validar el form
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		person = Person.objects.create(
			first_name=data['first_name'],
			father=data['father'],
			)
		#Hasta que el objecto no este creado no podemos enlazarlo por eso nacionality va aparte
		for country in data['nacionality']:
			person.nacionality.add(country)

		return JsonResponse({
			'name': person.first_name,
			'father': str(person.father),
			'nacionality': ','.join([str(country) for country in person.nacionality.all()]),
			})
	return render(request, "people/register.html", {'form':form})