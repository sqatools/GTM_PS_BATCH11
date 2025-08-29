# multiple inheritance
class GrandFather:
    def __init__(self, gf_name, gf_property):
        self.grandfather_name = gf_name
        self.grandfather_property = gf_property

    def grandfather_details(self):
        print("GrandFather Name :", self.grandfather_name)
        print("GrandFather Business :", self.grandfather_property)


class Father(GrandFather):
    def __init__(self, f_name, f_business, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.father_name = f_name
        self.father_business = f_business

    def father_details(self):
        print("Father Name :", self.father_name)
        print("Father Business :", self.father_business)


# child/derived class
# MRO : Method resolution order means, the constructor of class to be initialized in the child class constructor
#       will get priority on the basic of order of class being called during setup of inheritance

class Son(Father):
    """
        when we set up inheritance between two classes, then we have to initialize the parent
        class constructor inside the child class constructor with the help super keyword.

        """

    def __init__(self, son_name, f_name, f_business, gf_name, gf_property):
        super().__init__(f_name, f_business, gf_name, gf_property)
        self.son_name = son_name

    def son_details(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.father_details()
        self.grandfather_details()
        self.son_details()


obj = Son("Ram", "Rao", "Construction", "Raj", "House")
obj.family_details()

"""
Father Name : Rao
Father Business : Construction
GrandFather Name : Raj
GrandFather Business : House
Son Name : Ram
"""
