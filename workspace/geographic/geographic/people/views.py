from django.shortcuts import render
from django.http import JsonResponse
from people.forms import RegisterForm

# Create your views here.
def register(request):
	#mandando request.POST podemos validar el form
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		return JsonResponse(form.cleaned_data)
	return render(request, "people/register.html", {'form':form})