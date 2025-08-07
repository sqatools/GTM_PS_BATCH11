class Student:

    city = "Dehradun"
    state = "UK"

    def __init__(self, name, roll_no, standard):
        self.name = name
        self.roll_no = roll_no
        self.standard = standard
        print(self.name)
        print(self.roll_no)
        print(self.standard)

    def show(self):
        print(self.city)
        print(self.state)

    def sumation(self, n1, n2):
        print("sum of two numbers is :: ", n1 + n2)

    def substarction(self, n1, n2):
        print("the difference of two numbers is :: ", n1 - n2)

    def greeting(self):
        print("Hello Team Good Morning")

    def show_city_name(self):
        print("city name :", self.city)
        self.city = "Mumbai"
        print("city name :", self.city)

    def city_name(self):
        print(self.city)
        print(self.state)

obj = Student("vipul", 36, "6th")
obj.show()
obj.sumation(10, 20)
obj.substarction(10, 20)
Student.greeting(obj)
obj.greeting()
obj.show_city_name()
obj1 = Student("vipul", 36, "6th")
obj1.city_name()
obj1.city_name()

