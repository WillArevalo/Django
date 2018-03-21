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
	father = forms.ModelChoiceField(required=False,queryset=Person.objects.all())

#Formulario semiautomatico
class RegisterFormModel(forms.ModelForm):
	# Si definieramos aqui model lo tomaria como una variable y no como un modelo,
	# por eso lo hacemos desde una clase

	#Son casos muy específicos donde necesitas personalizar comportamientos o datos iniciales de un formulario dependiendo de lo que necesitas.
	def __init__(self, fathers, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['father'].queryset = fathers

	# El modelFrom determina si un campo es obligatorio por el atributo blank en el modelo, mas no el atributo null
	class Meta:
		model = Person
		fields = ['first_name','nacionality', 'father']