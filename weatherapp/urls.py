from . import views
from django.urls import path

urlpatterns = [
    path('', views.weatherHome, name='weatherhome'),
    path('<city>/', views.cityDetail, name='citydetail'),
]
