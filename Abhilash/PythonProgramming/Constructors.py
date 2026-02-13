# Constructor

# class myclass:
#     def __init__(self):
#         print("This is constructor....")
#     def n1(self):
#         print("hello...")
#     def n2(self,x,y):
#         return (x+y)
# mc=myclass()   # invoke constructor automatically
# mc.n1()        # method we have call explicity by using object
# print(mc.n2(20,40))  # 60

# Example

# class Emp:
#     def __init__(self,empid,ename,salary):
#         self.empid = empid
#         self.ename = ename
#         self.salary = salary
#     def display(self):
#         print(self.empid,self.ename,self.salary)
#
# e1=Emp(101,"Abhi",1000000)
# e2=Emp(102,"Bujji",500000)
# e1.display()  # 101 Abhi 1000000
# e2.display()  # 102 Bujji 500000


# grade = "Pass"  # Global Variable
# def results():
#     grade = "Fail"  # local to global
#     print(grade)
#
# re = results()
# print(grade)   # Fail Pass


# Create a parent class Animal with an __init__ that takes name
# Add a method speak that prints the name
# Create a child class Dog that inherits from Animal
# Create an object d1 = Dog("Rex")
# Call d1.speak()

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
            print(self.name)
class Dog(Animal):
    pass

d1= Dog("Rex")
d1.speak()





