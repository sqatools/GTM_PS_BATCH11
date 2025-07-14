"""
class: class is the blueprint of the object, where we define all typeof attributes/properties/variables/methods
       for specific object.

object: object is an entity to access all property/attribute of the class.

method: When we write a function inside the class, then it is called method.

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

variable:




"""
# create a class
class ABC:

    def __init__(self, n1, n2):
        print("------ WELCOME TO ABC CLASS -------")
        self.v1 = n1 # instance variable
        self.v2 = n2 # instance variable

    # create a method
    def show_msg(self, msg):
        print(msg)

    # instance method
    def addition(self, num1, num2):
        print("addition :", num1+num2)


    def greeting(self):
        print("Welcome to OOPS concepts")


    def sum_of_v1_and_v2(self):
        print("Addition of v1, v2:", self.v1 + self.v2)




# create an object of ABC class.
obj = ABC(100, 200)

# access the method with the help of object
obj.show_msg("Learning Python")
obj.addition(40, 50)
####################################
# What is self :  self is nothing but the object of current class being created
#                 ->  when we call any instance with the help of object, then object of the class is first parameter
#                     internally to the method, no need to specify while calling the method.

#obj.greeting()
ABC.greeting(obj)

###################################

obj.sum_of_v1_and_v2()
