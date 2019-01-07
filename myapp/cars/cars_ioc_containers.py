"""Dependency injection example, Cars & Engines IoC containers."""

from . import cars
from . import engines

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Engines(containers.DeclarativeContainer):
    """IoC container of engine providers."""
    gasoline = providers.Factory(engines.GasolineEngine)
    diesel = providers.Factory(engines.DieselEngine)
    electro = providers.Factory(engines.ElectroEngine)


class Cars(containers.DeclarativeContainer):
    """IoC container of car providers."""
    gasoline = providers.Factory(cars.Car, engine=Engines.gasoline)
    diesel = providers.Factory(cars.Car, engine=Engines.diesel)
    electro = providers.Factory(cars.Car, engine=Engines.electro)


if __name__ == '__main__':
    gasoline_car = Cars.gasoline()
    diesel_car = Cars.diesel()
    electro_car = Cars.electro()