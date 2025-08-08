

class Batch11:
    city_name = "Bangalor"
    def __init__(self,v1,v2):
        "--Welcome to the Batch11--"
        self.square(5)
        self.var1 = v1
        self.var2 = v2
    def greetings(self,msg):
        print(msg)
    def addition(self):
        self.var3 = 100 # instance variable
        print("addition of two numbers:",self.var1+self.var2)

    def show_v3(self):
        print(self.var3)


#self is nothing but the object of the current class
#method with the word self is known as instance method
#instance variable is a Global variable that can be used in different methods
#any variable that starts with self is known as instance variable
    def square(self,n):
        print("square value:",n**2)
    @classmethod
    def show_city_name(cls):
        print("Cityname :",cls.city_name)

    @staticmethod

#create class object
ln = Batch11(10,20)
ln.greetings("We are learning Python OOPS")
ln.show_v3()
# Construction = Initializes the

