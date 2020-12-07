from django.core.checks import messages
from django.http import response
from django.shortcuts import redirect, render
import requests
import json
from .models import City
from .forms import CityForm




def weatherHome(request):
    url = "https://api.weatherapi.com/v1/forecast.json?key=0a0c313f1ae24d41ab340802202911&q={}&days=3"

    # searched_cityweather = []
    # searched_singlecity_weatherdata = []
    # myerro_message = []

    # if request.method == "POST":
    #     form = CityForm(request.POST)
    #     if form.is_valid():
    #         newcity = form.cleaned_data['name']
    #         response = requests.get(url.format(newcity))
    #         r = response.json()

  



    form = CityForm()

    weatherdata_list = []
    singlecity_weather_data = []
    

    "for single city weather data "
    singlecityobj = City.objects.get(pk=3)
    city = singlecityobj
    response = requests.get(url.format(city))
    r = response.json()
    weatherdata = {
            'city': city,
            'region':r['location']['region'],
            'country':r['location']['country'],
            'localtime':r['location']['localtime'],
            'temp_c':r['current']['temp_c'],
            'temp_f':r['current']['temp_f'],
            'description':r['current']['condition']['text'],
            'icon':r['current']['condition']['icon'],
            'wind_mph':r['current']['wind_mph'],
            'wind_kph':r['current']['wind_kph'],
            'wind_dir':r['current']['wind_dir'],
            'pressure_mb':r['current']['pressure_mb'],
            'pressure_in':r['current']['pressure_in'],
            'precip_in':r['current']['precip_in'],
            'precip_mm':r['current']['precip_mm'],
            'humidity':r['current']['humidity'],
            'feelslike_c':r['current']['feelslike_c'],
            
            'feelslike_f':r['current']['feelslike_f'],


        }    

    singlecity_weather_data.append(weatherdata)




    cityobject = City.objects.all()
    
    for city in cityobject:
        response = requests.get(url.format(city))
        r = response.json()
        if 'error' in r:
            err_msg = 'database error'
            # return redirect('weatherhome')
        
        else:

            weatherdata = {
                'city': city,
                'region':r['location']['region'],
                'country':r['location']['country'],
                'localtime':r['location']['localtime'],
                'temp_c':r['current']['temp_c'],
                'temp_f':r['current']['temp_f'],
                'description':r['current']['condition']['text'],
                'icon':r['current']['condition']['icon'],
                'wind_mph':r['current']['wind_mph'],
                'wind_kph':r['current']['wind_kph'],
                'wind_dir':r['current']['wind_dir'],
                'pressure_mb':r['current']['pressure_mb'],
                'pressure_in':r['current']['pressure_in'],
                'precip_in':r['current']['precip_in'],
                'precip_mm':r['current']['precip_mm'],
                'humidity':r['current']['humidity'],
                'feelslike_c':r['current']['feelslike_c'],
                
                'feelslike_f':r['current']['feelslike_f'],


            }    

            weatherdata_list.append(weatherdata)


        # for single page weather info in weather home
        


    context = {
        "singlecity_weather_data":singlecity_weather_data,        
        'weatherdata_list':weatherdata_list,
        'form':form,
        
    }


    return render(request, 'weatherapp/weatherhome.html', context)



def cityDetail(request, city):
    url = "https://api.weatherapi.com/v1/forecast.json?key=0a0c313f1ae24d41ab340802202911&q={}&days=3"
    
    err_msg=""
    message = " "
    message_class = " "
    weatherdata1day_list = []
    weatherdata3days_list = []
    average_weatherdata3day_list = []  
    searched_cityweather = [] 
    searched_weatherdata3days_list = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            
            newcity = form.cleaned_data['name']
            formresponse = requests.get(url.format(newcity))
            r = formresponse.json()
            if 'error' in r:
                err_msg = 'city not found'
            else:
                
                weatherdata = {
                    'city': newcity.name,
                    'region':r['location']['region'],
                    'country':r['location']['country'],
                    'localtime':r['location']['localtime'],
                    'temp_c':r['current']['temp_c'],
                    'temp_f':r['current']['temp_f'],
                    'description':r['current']['condition']['text'],
                    'icon':r['current']['condition']['icon'],
                    'wind_mph':r['current']['wind_mph'],
                    'wind_kph':r['current']['wind_kph'],
                    'wind_dir':r['current']['wind_dir'],
                    'pressure_mb':r['current']['pressure_mb'],
                    'pressure_in':r['current']['pressure_in'],
                    'precip_in':r['current']['precip_in'],
                    'precip_mm':r['current']['precip_mm'],
                    'humidity':r['current']['humidity'],
                    'feelslike_c':r['current']['feelslike_c'],
                    
                    'feelslike_f':r['current']['feelslike_f'],


                }    

                searched_cityweather.append(weatherdata)
                with open('searched_data.json', 'w') as myfile:
                    json.dump(searched_cityweather, myfile, indent=4)
                
                for data in r['forecast']['forecastday']:
                    for rsp in data['hour']:
                        weatherdata = {
                        'city': newcity.name,
                        'alldatetime':rsp['time'],
                        'alltemp_c':rsp['temp_c'],
                        'alltemp_f':rsp['temp_f'],
                        'alldescription':rsp['condition']['text'],
                        'allicon':rsp['condition']['icon'],
                        'allwind_mph':rsp['wind_mph'],
                        'allwind_kph':rsp['wind_kph'],
                        'allwind_dir':rsp['wind_dir'],
                        'allpressure_mb':rsp['pressure_mb'],
                        'allpressure_in':rsp['pressure_in'],
                        'allprecip_in':rsp['precip_in'],
                        'allprecip_mm':rsp['precip_mm'],
                        'allhumidity':rsp['humidity'],
                        'allfeelslike_c':rsp['feelslike_c'],
                        'allfeelslike_f':rsp['feelslike_f'],
                        'allwill_it_rain':rsp['will_it_rain'],
                        'allchance_of_snow':rsp['chance_of_snow'],
                    }    

                    searched_weatherdata3days_list.append(weatherdata)
   

    form = CityForm()
    

    city = City.objects.get(name=city)

    response = requests.get(url.format(city)).json()

    # single day weather data
    weatherdata = {
        'city': city.name,
        'region':response['location']['region'],
        'country':response['location']['country'],
        'localtime':response['location']['localtime'],
        'temp_c':response['current']['temp_c'],
        'temp_f':response['current']['temp_f'],
        'description':response['current']['condition']['text'],
        'icon':response['current']['condition']['icon'],
        'wind_mph':response['current']['wind_mph'],
        'wind_kph':response['current']['wind_kph'],
        'wind_dir':response['current']['wind_dir'],
        'pressure_mb':response['current']['pressure_mb'],
        'pressure_in':response['current']['pressure_in'],
        'precip_in':response['current']['precip_in'],
        'precip_mm':response['current']['precip_mm'],
        'humidity':response['current']['humidity'],
        'feelslike_c':response['current']['feelslike_c'],
        
        'feelslike_f':response['current']['feelslike_f'],
    }    

    weatherdata1day_list.append(weatherdata)
    with open('singlecity.json', 'w') as myfile:
        json.dump(weatherdata1day_list, myfile, indent=4)




    
    # the average weather data for 3 days 
    for data in response['forecast']['forecastday']:
        
        weatherdata = {
            'city': city.name,


            'datetime':data['date'],
            'maxtemp_c':data['day']['maxtemp_c'],
            'maxtemp_f':data['day']['maxtemp_f'],
            'mintemp_c':data['day']['mintemp_c'],
            'mintemp_f':data['day']['mintemp_f'],
            'avgtemp_c':data['day']['avgtemp_c'],
            'avgtemp_f':data['day']['avgtemp_f'],
            'description':data['day']['condition']['text'],
            'icon':data['day']['condition']['icon'],
            'maxwind_mph':data['day']['maxwind_mph'],
            'maxwind_kph':data['day']['maxwind_kph'],
            'totalprecip_in':data['day']['totalprecip_in'],
            'totalprecip_mm':data['day']['totalprecip_mm'],
            'avghumidity':data['day']['avghumidity'],
            'daily_will_it_rain':data['day']['daily_will_it_rain'],
            'daily_chance_of_snow':data['day']['daily_chance_of_snow'],
            # additional weather info
            'sunrise':data['astro']['sunrise'],
            'sunset':data['astro']['sunset'],
            'moonrise':data['astro']['moonrise'],
            'moonset':data['astro']['moonset'],
            'moonphase':data['astro']['moon_phase'],
            'moonillumination':data['astro']['moon_illumination'],

        }    

        average_weatherdata3day_list.append(weatherdata)
        


        # three day weather condition
    for data in response['forecast']['forecastday']:
        for r in data['hour']:
            weatherdata = {
                'city': city.name,
                'alldatetime':r['time'],
                'alltemp_c':r['temp_c'],
                'alltemp_f':r['temp_f'],
                'alldescription':r['condition']['text'],
                'allicon':r['condition']['icon'],
                'allwind_mph':r['wind_mph'],
                'allwind_kph':r['wind_kph'],
                'allwind_dir':r['wind_dir'],
                'allpressure_mb':r['pressure_mb'],
                'allpressure_in':r['pressure_in'],
                'allprecip_in':r['precip_in'],
                'allprecip_mm':r['precip_mm'],
                'allhumidity':r['humidity'],
                'allfeelslike_c':r['feelslike_c'],
                'allfeelslike_f':r['feelslike_f'],
                'allwill_it_rain':r['will_it_rain'],
                'allchance_of_snow':r['chance_of_snow'],
            }    

            weatherdata3days_list.append(weatherdata)
            with open('singlecity.json', 'w') as myfile:
                json.dump(weatherdata1day_list, myfile, indent=4)
    

    context={
        'weatherdata3days_list':weatherdata3days_list,
        'average_weatherdata3day_list':average_weatherdata3day_list,
        'weatherdata1day_list': weatherdata1day_list ,
        'searched_cityweather': searched_cityweather,
        "searched_weatherdata3days_list":searched_weatherdata3days_list,
        'form':form,
        'message':message,
        'message_class': message_class,
        
        
    }

    return render(request, 'weatherapp/citydetail.html', context)




# def add_to_favorite(request, city):
#     url = "https://api.weatherapi.com/v1/forecast.json?key=0a0c313f1ae24d41ab340802202911&q={}&days=3"
#     err_msg = ''
#     message = ''
#     message_class = ''
    
    
#     searched_cityweather = []
#     if request.method =="POST":
#         form = CityForm(request.POST)

#         if form.is_valid():
            
#             city = form.cleaned_data['name']              
#             r = requests.get(url.format(city)).json()


            
#             if 'error' in r:
#                 err_msg = 'city not found'
                
            
#             else: 
                
#                 weatherdata = {
#                 'city': city,
#                 'region':r['location']['region'],
#                 'country':r['location']['country'],
#                 'localtime':r['location']['localtime'],
#                 'temp_c':r['current']['temp_c'],
#                 'temp_f':r['current']['temp_f'],
#                 'description':r['current']['condition']['text'],
#                 'icon':r['current']['condition']['icon'],
#                 'wind_mph':r['current']['wind_mph'],
#                 'wind_kph':r['current']['wind_kph'],
#                 'wind_dir':r['current']['wind_dir'],
#                 'pressure_mb':r['current']['pressure_mb'],
#                 'pressure_in':r['current']['pressure_in'],
#                 'precip_in':r['current']['precip_in'],
#                 'precip_mm':r['current']['precip_mm'],
#                 'humidity':r['current']['humidity'],
#                 'feelslike_c':r['current']['feelslike_c'],
                
#                 'feelslike_f':r['current']['feelslike_f'],


#                 }  
#                 with open('forweather.json', 'w') as myfile:
#                     json.dump(searched_cityweather, myfile, indent=4)  

#                 searched_cityweather.append(weatherdata)
                

        # if err_msg:
        #     message = err_msg
        #     message_class = 'is_danger'
    
    

    # context = {'message':message, 
    #             'message_class':message_class,
    #             'searched_cityweather':searched_cityweather,
                

    # }
    
          
    # return context
