from django.http import HttpResponse
from . import cars
from . import engines
import sys


def index(request):

    gasoline_car = cars.Car(engines.GasolineEngine())
    diesel_car = cars.Car(engines.DieselEngine())
    electro_car = cars.Car(engines.ElectroEngine())

    sys.stdout.write('gasoline_car detail : ' + str(gasoline_car._engine))
    sys.stdout.write('diesel_car detail : ' + str(diesel_car._engine))
    sys.stdout.write('electro_car detail : ' + str(electro_car._engine))
    
    text = """Nothing here!"""
    return HttpResponse(text)