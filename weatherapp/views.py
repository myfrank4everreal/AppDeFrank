from django.shortcuts import render


def weatherHome(request):
    context = {}

    return render(request, 'weatherapp/homepage.html', context)
