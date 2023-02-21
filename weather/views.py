import requests
from django.shortcuts import render
#from .models import City
#from .forms import CityForm

def index(request):
    appid = '028d35cd709183d538728f22bd991f7c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=' + appid

    url2 = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&lang=ru&appid=' + appid



    
    city = 'Los Angeles'

    city = request.POST['city']
    
    #all_cities = []
    #for city in cities:
    res = requests.get(url.format(city)).json()
    import time
    sunrise = time.gmtime(res["sys"]["sunrise"])
    risehour = sunrise.tm_hour
    risemin = sunrise.tm_min
    
    sunset = time.gmtime(res["sys"]["sunset"])
    sethour = sunset.tm_hour
    setmin = sunset.tm_min

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'main': res["weather"][0]["main"],
        'wind': res["wind"]["speed"],
        'humidity': res["main"]["humidity"],
        'pressure': res["main"]["pressure"],
        'risehour': risehour, #res["sys"]["sunrise"],
        'risemin': risemin,
        'sethour': sethour, #res["sys"]["sunrise"],
        'setmin': setmin,
        'icon': res["weather"][0]["icon"]

    }

    res2 = requests.get(url2.format(city)).json()
    
    forecast_info = {
        'city': city,
        'temp': res2["list"][0]["main"]["temp"]
        
    }




    #all_cities.append(city_info)
    #all_cities = city_info

    #context = {'all_cities': all_cities, 'form': form}
    context = {'info': city_info, 'forecast_info': forecast_info}
    

    return render(request, 'weather/index.html', context)





#if(request.method == 'POST'):
    #    form = CityForm(request.POST)
    #    form.save()

    #form = CityForm()

    #res1 = requests.post(url.format(city)).json()
    
    #cities = City.objects.all()