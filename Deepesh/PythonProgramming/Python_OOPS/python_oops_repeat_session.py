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



# What is self :  self is nothing but the object of current class being created

"""
class Batch11:
    city_name = "Bangalore"


    def __init__(self, v1, v2):
        print("-- Welcome to Batch11 --")
        self.square(5)
        self.var1 = v1 #  self.var1 is instance variable
        self.var2 = v2 #  self.var1 is instance variable


    def greeting(self, msg):
        print(msg)


    def square(self, n):
        print("square value :", n**2)

    def addition(self):
        self.var3 = 100 # instance variable in method
        print("addition of values :", self.var1 + self.var2)

    def show_v3(self):
        self.addition()
        print(self.var3)

    @classmethod
    def show_city_name(cls):
        print("Cityname :", cls.city_name)

    def show_city_name_instance(self):
        print("City Name :", self.city_name)

    @staticmethod
    def get_factorials(n):
        fact = 1
        for i in range(5, 0, -1):
            fact *= i

        print(f"factorials of {n} :", fact)




# # create class object
# obj = Batch11(30, 40)
# # calling the method with object
# obj.greeting('We are Learning Python OOPS')
# obj.square(10)
# obj.show_v3()


Batch11.show_city_name()
Batch11.get_factorials(5)

