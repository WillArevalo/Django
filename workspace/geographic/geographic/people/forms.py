from django import forms

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='first name')
	occupation = forms.CharField(label='occupation')