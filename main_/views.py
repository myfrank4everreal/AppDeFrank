from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "main_/index.html", context)




