from unicodedata import name
from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import cityForm
from django.contrib import messages
import json

# Create your views here.

def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c1f89d0b82f356c1c3ac4eff2809b1f3'

    cities = City.objects.all()
    weatherData = []
    
    if request.method=='POST':
        
        form = cityForm(request.POST)
        if form.is_valid():
            form.save()
    form = cityForm()
    for city in cities:
        r=requests.get(url.format(city.name)).json()

        if r['cod']=='404':
            messages.error(request,"city not found!!")
            City.objects.filter(name=city.name).delete()
            return redirect('/')

        else :
            cityWeather = {
            'city':city.name,
           'temperature': r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'cityid':city.id,
            }

            weatherData.append(cityWeather)
    context={
        'weatherData':weatherData,
        'form':form,
            }

    return render(request,'index.html',context)

def delobj(request,objId):
    event = City.objects.get(pk=objId)
    event.delete()
    return redirect('/') 

def delAll(request):
    City.objects.all().delete()
    return redirect('/')