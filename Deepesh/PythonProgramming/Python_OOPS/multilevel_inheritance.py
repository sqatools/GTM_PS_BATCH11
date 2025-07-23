"""
# inheritance : when one class aquare the property of another class, then it is inheritance

1. single inheritance : class A ->  Class B
2. multilevel inheritance : class A -> class B -> class C
3. multiple inheritance :
4. Hierarchical inheritance :

"""

# multilevel inheritance
class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.grandfather_name = gf_name
        self.grandfather_property = gf_property

    def show_grandfather_details(self):
        print("Grand Father Name :", self.grandfather_name)
        print("Grand Father Property :", self.grandfather_property)



# parent/base/super class
class Father(GrandFather):
    def __init__(self, f_name, f_house, f_business, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.father_name = f_name
        self.father_house = f_house
        self.father_business = f_business

    def show_father_details(self):
        print("Father Name :", self.father_name)
        print("Father House :", self.father_house)
        print("Father Business :", self.father_business)


# setup inheritance between Father and Son class
# child/derived class
class Son(Father):
    """
    when we setup inheritance between two classes, then we have to initialize the parent
    class constructor inside the child class constructor with the help super keyword.

    """

    def __init__(self, son_name, f_name, f_house, f_business, gf_name, gf_property):
        # initializing the parent class constructor inside the child class
        super().__init__(f_name, f_house, f_business, gf_name, gf_property)
        self.son_name = son_name

    def show_son_name(self):
        print("Son name :", self.son_name)

    def show_family_details(self):
        self.show_grandfather_details()
        self.show_father_details()
        self.show_son_name()


obj = Son('Rahul', 'Vinod Gupta', 'Banglow', 'Construction', 'Ram Dayal', '200 Acr')
obj.show_family_details()
