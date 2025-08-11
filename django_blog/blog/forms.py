# Creating CUSTOM REGISTRATION FORM and extend UserCreationForm to add the email field.
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class meta(UserCreationForm.Meta):
    fields = UserCreationForm.Meta.fields + ('email',)
