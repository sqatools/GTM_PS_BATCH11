"""
# inheritance : when one class aquare the property of another class, then it is inheritance

1. single inheritance : class A ->  Class B
2. multilevel inheritance :
3. multiple inheritance :  class A ->  class B, class C ->  class B
4. Hierarchical inheritance :

"""


# multiple inheritance :
class Mother:
    def __init__(self, m_name, m_business):
        self.mother_name = m_name
        self.mother_business = m_business

    def show_mother_details(self):
        print("Mother Name :", self.mother_name)
        print("Mother Business :", self.mother_business)



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



# child/derived class
# MRO : Method resolution order means, the constructor of class to be initialized in the child class constructor
#       will get priority on the basic of order of class being called during setup of inheritance
class Son(Father, Mother):
    """
    when we setup inheritance between two classes, then we have to initialize the parent
    class constructor inside the child class constructor with the help super keyword.

    """

    def __init__(self, son_name, f_name, f_house, f_business, m_name, m_business):
        super().__init__(f_name, f_house, f_business)
        self.mother_name = m_name
        self.mother_business = m_business
        self.son_name = son_name

    def show_son_name(self):
        print("Son name :", self.son_name)

    def show_family_details(self):
        self.show_father_details()
        self.show_mother_details()
        self.show_son_name()


obj = Son('Rahul', 'Vinod Gupta', 'Banglow', 'Construction', "Pooja Gupta", "Fashion")
obj.show_family_details()
"""
Father Name : Vinod Gupta
Father House : Banglow
Father Business : Construction
Mother Name : Pooja Gupta
Mother Business : Fashion
Son name : Rahul
"""