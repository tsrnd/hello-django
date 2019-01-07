"""Dependency injection example, engines module."""


class Engine(object):
    """Example engine base class.
    Engine is a heart of every car. Engine is a very common term and could be
    implemented in very different ways.
    """


class GasolineEngine(Engine):
    """Gasoline engine."""


class DieselEngine(Engine):
    """Diesel engine."""


class ElectroEngine(Engine):
    """Electro engine."""