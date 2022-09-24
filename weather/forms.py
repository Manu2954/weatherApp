from turtle import textinput
from django.forms import ModelForm,TextInput
from .models import City

class cityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class':'form-control','placeholder':'search for a city','id':'inp','name':'search','autocomplete':'new-password'})}