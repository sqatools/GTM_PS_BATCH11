# Encapsulation or Data Hiding
"""

"""

class Car:
    def __init__(self, car_name, car_company, car_price):
        self.car_name = car_name
        self._car_company = car_company
        self.__car_price = car_price

    def show_car_name(self):
        print("Car Name :", self.car_name)

    def _show_car_company(self):
        print("Car Company :", self._car_company)

    def __show_car_price(self):
        print("Car Price :", self.__car_price)


obj = Car('Creta', 'Hyundai', '18 Lacs')
obj.show_car_name()
obj._show_car_company()
obj._Car__show_car_price()
"""
Car Name : Creta
Car Company : Hyundai
Car Price : 18 Lacs
"""


