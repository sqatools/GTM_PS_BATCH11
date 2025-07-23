"""
Encapsulation/Data Hiding :  This is the process the bind the class and data member in one single unit and restrict to access
# the class data outside of the class.

# We can achieve data hiding in python with the help of single underscore (_) or double underscore (__)as prefix in the variable or anyh method.
"""

class Car:
    def __init__(self, car_name, car_comp, car_price):
        self.car_name = car_name
        self._car_company = car_comp
        self.__car_price = car_price

    def show_car_name(self):
        print("Car Name :", self.car_name)

    def _show_car_company(self):
        print("Car Company :", self._car_company)

    def __show_car_price(self):
        print("Car price :", self.__car_price)



obj = Car("Harrier", "TATA", "25 Lac")
obj.show_car_name()

# if we defined variable/method with single/double underscore as prefix, then those data member will not show in suggestion
# list of object data member.

# Access method variable/method with single underscore prefix
obj._show_car_company()


# Access method variable/method with double underscore prefix
# e.g obj._classname__variable/method
obj._Car__show_car_price()

print(dir(obj))
# ['_Car__car_price', '_Car__show_car_price', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_car_company', '_show_car_company', 'car_name', 'show_car_name']








