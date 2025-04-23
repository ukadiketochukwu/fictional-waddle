from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import LogisticUser

class UserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=LogisticUser.ROLE_CHOICES)

    class Meta:
        model = LogisticUser
        fields = ('username', 'email', 'role', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
