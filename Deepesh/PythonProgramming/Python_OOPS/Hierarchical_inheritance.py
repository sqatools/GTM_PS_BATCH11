"""
# inheritance : when one class aquare the property of another class, then it is inheritance

1. single inheritance : class A ->  Class B
2. multilevel inheritance :
3. multiple inheritance :
4. Hierarchical inheritance : class A -> class B, class A -> class C

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


# setup inheritance between Father and Son class
# child/derived class
class Son1(Father):
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



class Son2(Father):
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


obj = Son1('Rahul', 'Vinod Gupta', 'Banglow', 'Construction')
obj.show_family_details()

"""
Father Name : Vinod Gupta
Father House : Banglow
Father Business : Construction
Son name : Rahul
"""

print("_"*50)
obj2 = Son2("Mohit", "Vinod Gupta", "4 BHK", "Construction")
obj2.show_family_details()

"""
Father Name : Vinod Gupta
Father House : 4 BHK
Father Business : Construction
Son name : Mohit
"""