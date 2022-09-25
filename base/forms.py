from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].help_text='<br> <b>Password should be 8 characters long.</b>'
		self.fields['password2'].help_text=''
		self.fields['username'].help_text=''

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user