from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    city=request.GET.get('city',"Lucknow")
    url= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fa40108cca5260c8eb0e3ed09d94da25'
    data= requests.get(url).json()
   # print(data)
    payload= {'city' : data['name'],
              'weather' : data['weather'][0]['main'],
              'icon' : data['weather'][0]['icon'],
              'kelvin_temperature' : int(data['main']['temp']),
              'celsius_temperature' : int(data['main']['temp'])-273,
              'pressure' : data['main']['pressure'],
              'humidity' : data['main']['humidity'],
              'description' : data['weather'][0]['description'],
              }
    context = {'data' : payload}
    print(context)
    return render(request,'home.html',context)