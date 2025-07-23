"""
polymorphism : when one particular method or variable performing multiple tasks, then it is called polymorphism.
1. Method overriding : When two classes are connected via inheritance and both the class have method with same name
                      then child class method will override the parent class method.
                      if we call the method with child class object, then class method will get priority.
2. Method overloading : Python does not support method overloading
                       ->  When one class has two method with same name and different parameters, then it is called
                           method overloading.
                       ->  If define such scenario in python, it will only consider the latest defined method.

3. Operator Overloading : when one operator perform multiple tasks, then it is called operator overloading
                      e,g. Plus operator  can add 2 number, it can concatenate 2 string, it can also combine list.


"""


# single inheritance :
# parent/base/super class
class Father:
    def __init__(self, f_name, f_house, f_business):
        self.father_name = f_name
        self.father_house = f_house
        self.father_business = f_business

    def show_father_details(self):
        print("Father Name :", self.father_name)
        print("Father House :", self.father_house)
        print("Father Business :", self.father_business)


    def greeting(self):
        print("____WELCOME TO FATHER CLASS___")
        print("We Are Learning From Father class")


    def addition(self, n1, n2):
        print("addition in father :", n1+n2)



# setup inheritance between Father and Son class
# child/derived class
class Son(Father):
    """
    when we setup inheritance between two classes, then we have to initialize the parent
    class constructor inside the child class constructor with the help super keyword.

    """

    def __init__(self, son_name, f_name, f_house, f_business):
        # initializing the parent class constructor inside the child class
        super().__init__(f_name, f_house, f_business)
        self.son_name = son_name

    def show_son_name(self):
        print("Son name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_son_name()

    def greeting(self):
        print("____WELCOME TO SON CLASS___")
        print("We Are Learning From SON class")


    def addition(self, n1, n2, n3):
        print("addition in son :", n1+n2+n3)


    def multiplication(self, v1, v2):
        print("multiplication 2 variables :", v1*v2)

    def multiplication(self, v1, v2, v3):
        print("multiplication 3 variables :", v1*v2*v3)



obj = Son('Rahul', 'Vinod Gupta', 'Banglow', 'Construction')
#obj.show_family_details()
obj.greeting()
obj.addition(40, 50, 60)

obj.multiplication(5, 6, 7)


################################## Operator overloading #################

n1 = 40
n2 = 50
print("addition :", n1+n2)
print("addition :", n1.__add__(n2))
print(dir(int))


print("_"*50)
s1 = 'Hello'
s2 = 'Good Morning'
print("result :", s1+s2)
print("result :", s1.__add__(s2))
print(dir(str))


print("_"*50)
l1 = [4, 6, 7]
l2 = [7, 9, 20]
print("result list :", l1.__add__(l2))
print(dir(list))