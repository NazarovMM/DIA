import unittest
from patterns.factorymethod import PlaneDelivery, CarDelivery


class proxyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Plane = PlaneDelivery()
        self.car = CarDelivery()
        print("Launched with the car.")

    def test_fueloutplane(self):
        self.assertEqual(self.Plane.devlivery_method(), "delivering can't be done no fuel.")
        self.Plane.refueling(20)
        self.assertEqual(self.Plane.devlivery_method(), "Pleas contact to dispatcher and update weather status")

    def test_weatherplane(self):
        listofusers = [ "средняя", "нормальная", "Хорошая"]
        for i in listofusers:
            with self.subTest(i=i):
                self.Plane.updateweather(i)
                self.assertEqual(self.Plane.checkweather(), 1)

    def test_deliveryplane(self):
        self.Plane.refueling(20)
        self.Plane.updateweather("Хорошая")
        self.assertEqual(self.Plane.devlivery_method().operation(), "Coal are delivered")

    def test_carfuel(self):
        self.assertEqual(self.car.devlivery_method(), "delivering can't be done no fuel.")
    def test_cardelivery(self):
        self.car.refueling(10)
        self.assertEqual(self.car.devlivery_method().operation(), "Wood are delivered")


if __name__ == '__main__':
    unittest.main()
