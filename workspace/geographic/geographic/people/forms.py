from django import forms
from countries.models import Country
from people.models import Person

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='first name')
	#email = forms.EmailField(label='email')
	#date = forms.DateField(label='date')
	#is_active = forms.BooleanField(label='active')
	#campos con modelos
	#Many to Many
	nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
	#One to Many
	father = forms.ModelChoiceField(queryset=Person.objects.all())