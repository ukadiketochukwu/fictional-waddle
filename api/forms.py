from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import LogisticUser
from .models import Truck, Load

class UserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=LogisticUser.ROLE_CHOICES)

    class Meta:
        model = LogisticUser
        fields = ('username', 'email', 'role', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['title', 'capacity', 'location']

class LoadForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = ['description', 'weight', 'pickup_location', 'dropoff_location']
