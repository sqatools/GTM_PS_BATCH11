# When a particular method and variable perform the multiple task then it is known as polymorphism.
# It contains two methods :: Method overloading and method over ridding
# Method over loading is not applicable in pyhton.

class Parent:
    def __init__(self, f_name, f_age):
        self.f_name = f_name
        self.f_age = f_age

    def show_details(self):
        print("Father's name :: ", self.f_name)
        print("Father's age :: ", self.f_age)

    def add(self, n1, n2):
        print("addition of two numbers is :: ", n1+n2)


class Son(Parent):
    def __init__(self, s_name, s_age, f_name, f_age):
        super().__init__(f_name, f_age)
        self.s_name = s_name
        self.s_age = s_age

    def show_details(self):
        print("Son's name is :: ", self.s_name)
        print("Son's age is :: ", self.s_age)


obj = Son("Vipul", 35, "Sukveer Singh", 65)
obj.show_details()
obj.add(5, 30)
obj1 = Parent("Sukveer Singh", 65)
obj1.show_details()
obj.f_name()
