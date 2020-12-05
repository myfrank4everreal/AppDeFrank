from django.shortcuts import render


def weatherHome(request):
    return render(request, 'weatherapp/weatherhome.html')



