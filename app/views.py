from django.shortcuts import render
import requests
def home(request):
    city = request.GET.get('city','ambala')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=40bb0a8e40ccd8b22e3c3c0f59fdb699'
    data = requests.get(url).json()
    payload = {'city': data['name'],
               'weather': data['weather'][0]['main'],
               'icon':data['weather'][0]['icon'],
               'kelvin_temperature':data['main']['temp'],
               'celcius_temperature': int(data['main']['temp']-273),
               'pressure':data['main']['pressure'],
               'humidity':data['main']['humidity'],
               'description':data['weather'][0]['main']
               }
    context = {'data':payload}
    print(context)
    return render(request, 'app/home.html',context)