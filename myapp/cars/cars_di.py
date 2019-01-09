"""Dependency injection example, Cars & Engines."""

from . import cars
from . import engines


if __name__ == '__main__':
    gasoline_car = cars.Car(engines.GasolineEngine())
    diesel_car = cars.Car(engines.DieselEngine())
    electro_car = cars.Car(engines.ElectroEngine())