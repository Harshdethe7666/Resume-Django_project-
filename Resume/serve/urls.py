from django.contrib import admin
from django.urls import path
from serve import views


urlpatterns = [
    path('services/',views.serv,name="services"),
]