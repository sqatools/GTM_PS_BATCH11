"""
class: class is the blueprint of the object, where we define all typeof attributes/properties/variables/methods
       for specific object.

object: object is an entity to access all property/attribute of the class.

method: When we write a function inside the class, then it is called method.
           # There are three type of methods
           1.  instance method:  when we define any method with self as first parameter, then it is called instance method.
              Example:  def addition(self, n1, n2):
                          print(n1+n2)


          2.  class method: when we define method with decorator @classmethod, then it is called class method.
                        @classmethod
             Example:   def show_city_name_class(cls):
                             print("city name :", cls.city)


          3.  static method :  when we define method without any default parameter and with the help of @staticmethod decorator
                               then it is called static method
                               ->  static methods are directly associated with class, no need to create object of the class
                                   to access the static method.
                         @staticmethod
            Example:     def print_table(num):
                             for i in range(1, 11):
                                print(i, "*", num, ":", i*num)




constructor :  constructor that initialize the memory for the object of the class.
               -> constructor will be called when we create object of the class
               1.  default constructor :  default constructor will be executed whenever we create object of the class

                   def __init___(self):
                        code

               2. Parametrize constructor :  when we pass parameters to constructor then it is called parametrize
                  constructor.
                  ->  we have pass the value to constructor parameter, when we create an object of the class.

                  def __init__(self, n1, n2):
                     self.v1 = n1
                     self.v2 = n2

                  n1, n2 :  parameters
                  self.v1, self.v2 : instance variable

variable: when we define variable inside the class, then it is called class member variable.
            There ara 2 type of variable
            1.  instance variable : when we define any variable with self inside the class, then it is called instance variable
                e.g   self.var1 = "hello"


            2.  class/static variable : when we define any variable on class level then and we have to provide some static value to
                          the variable, then it is called class variable





"""


# create a class
class ABC:
    city = "Mumbai"  # class/static variable
    country = "India"  # class/static variable

    def __init__(self, n1, n2):
        print("------ WELCOME TO ABC CLASS -------")
        self.v1 = n1  # instance variable
        self.v2 = n2  # instance variable

    # create a method
    def show_msg(self, msg):
        print(msg)

    # instance method
    def addition(self, num1, num2):
        print("addition :", num1 + num2)

    def greeting(self):
        print("Welcome to OOPS concepts")

    def sum_of_v1_and_v2(self):
        print("Addition of v1, v2:", self.v1 + self.v2)

    def show_city_name(self):
        print("city name :", self.city)
        self.city = "Pune"

    @classmethod
    def show_city_name_class(cls):
        print("city name :", cls.city)

    @staticmethod
    def print_table(num):
        for i in range(1, 11):
            print(i, "*", num, ":", i * num)




# create an object of ABC class.
obj = ABC(100, 200)

# access the method with the help of object
obj.show_msg("Learning Python")
obj.addition(40, 50)
####################################
# What is self :  self is nothing but the object of current class being created
#                 when we call any method with the help of object of the class,
#                 then object of the class is first parameter to the method internally.
#                 no need to specify object value as parameter while calling the method.

# obj.greeting()
# if we are calling the method with class name, then we have to provide object as self parameter value.
ABC.greeting(obj)

###################################

obj.sum_of_v1_and_v2()

print("_" * 50)
##############################
# access the class variable
print(obj.city)  # Mumbai
obj.city = "Chennai"
print(obj.city)  # Chennai

print(ABC.city)  # Mumbai

obj.show_city_name()  # Chennai
print(obj.city)  # Pune

print("_" * 50)
################################
# access the class method
obj.show_city_name_class() # Mumbai
ABC.show_city_name_class() # Mumbai

print("_" * 50)
################################
# access the static method with object and class
obj.print_table(5)
ABC.print_table(6)


print("_" * 50)
################################
# getter and setter method
print(obj.__getattribute__("city")) # Pune

obj.__setattr__("v1", 500)
print("value of v1:", obj.v1) # value of v1: 500

