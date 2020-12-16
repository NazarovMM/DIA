from __future__ import annotations
from abc import ABC, abstractmethod

"пораждающий паттерн"


class Deliver(ABC):
    @abstractmethod
    def devlivery_method(self):
        pass

    def some_operation(self) -> str:
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        delivery = self.devlivery_method()
        if type(delivery) == str:
            return f"DELIVER: {delivery}"
        else:
            result = f"DELIVER: The product {delivery.operation()}"
        return result


class PlaneDelivery(Deliver):
    dictofweather = {"Очень плохая погода": 0, "Плохая погода": 1, "средняя": 2, "нормальная": 3, "Хорошая": 4}

    def __init__(self):
        self._fuel = 0
        self._weather = None

    def prepareflight(self, fueltoadd, weather):
        self.refueling(fueltoadd)
        self.updateweather(weather)

    def updateweather(self, weather):
        if weather not in self.dictofweather.keys():
            print("Pls give right weather status")
        else:
            self._weather = weather

    def refueling(self, count):
        self._fuel += count

    def isfuel(self):
        if self._fuel >= 10:
            self._fuel -= 10
            return True
        else:
            return False

    def checkweather(self):
        if self._weather == None:
            return 0
        if self.dictofweather[self._weather] >= 2:
            return 1
        else:
            return -1

    def devlivery_method(self):
        if self.isfuel():
            if self.checkweather() > 0:
                return Coal()
            elif self.checkweather() == -1:
                return "Sorry, can't deliver your product due to weahter."
            else:
                return "Pleas contact to dispatcher and update weather status"
        else:
            return "delivering can't be done no fuel."


class CarDelivery(Deliver):
    def __init__(self):
        self._fuel = 0

    def isfuel(self):
        if self._fuel >= 5:
            self._fuel -= 5
            return True
        else:
            return False

    def refueling(self, count):
        self._fuel += count

    def devlivery_method(self):
        if self.isfuel():
            return Wood()
        else:
            return "delivering can't be done no fuel."


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class Coal(Product):
    def operation(self) -> str:
        return "Coal are delivered"


class Wood(Product):
    def operation(self) -> str:
        return "Wood are delivered"


def client_code(deliver: Deliver) -> None:
    print(f"Client: I'm don't now who is deliver exactly.\n"
          f"{deliver.some_operation()}")


if __name__ == "__main__":
    Plane = PlaneDelivery()
    car = CarDelivery()
    print("Launched with the car.")
    client_code(car)
    print("")
    print("Launched with the Plane.")
    client_code(Plane)
    Plane.refueling(100)
    Plane.updateweather("Хорошая")
    client_code(Plane)
