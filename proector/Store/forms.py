from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required = True)
	class Meta:
		fields = ("username", "email", "password1", "password2")
		model = User