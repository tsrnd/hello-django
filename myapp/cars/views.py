from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .car_ioc import Cars


def index(request):
    gasoline_car = Cars.gasoline()
    responseStr = "Car Index " + gasoline_car._engine
    return HttpResponse.write(responseStr)
