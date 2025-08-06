# Polymorphism

class Father:
    def __init__(self, f_name, f_business):
        self.father_name = f_name
        self.father_business = f_business

    def father_details(self):
        print("Father Name :", self.father_name)
        print("Father Business :", self.father_business)

    def greetings(self):
        print("Welcome to Father Class")
        print("We are Learning Python")



# child/derived class
class Son1(Father):

    def __init__(self, son_name, f_name, f_business):
        super().__init__(f_name, f_business)
        self.son_name = son_name

    def son_details(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.father_details()
        self.son_details()

    # Method Overriding
    def greetings(self):
        print("Welcome to Son Class")
        print("We are Learning Python from Son Class")

    # Method Overloading
    def multiplication(self, v1, v2):
        print("Multiplication of 2 variables :", v1*v2)

    def multiplication(self, v1, v2, v3):
        print("Multiplication of 3 variables :", v1*v2*v3)



obj = Son1("Ram", "Rao", "Construction")
obj.family_details()
"""
Father Name : Rao
Father Business : Construction
Son Name : Ram
"""
obj.greetings()  # Welcome to Son Class # We are Learning Python from Son Class
obj.multiplication(2, 4, 6)  # Multiplication of 3 variables : 48

############## Operator Overloading ##############

n1 = 20
n2 = 30
print("Addition :", n1+n2)
print("Addition :", n1.__add__(n2))

s1 = 'Hello'
s2 = 'Good Morning'
print("Adding Strings :", s1+s2)
print("Adding Strings :", s1.__add__(s2))

