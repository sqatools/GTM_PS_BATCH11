# multiple inheritance
class Mother:
    def __init__(self, m_name, m_business):
        self.mother_name = m_name
        self.mother_business = m_business

    def mother_details(self):
        print("Mother Name :", self.mother_name)
        print("Mother Business :", self.mother_business)


class Father:
    def __init__(self, f_name, f_business):
        self.father_name = f_name
        self.father_business = f_business

    def father_details(self):
        print("Father Name :", self.father_name)
        print("Father Business :", self.father_business)


# child/derived class
# MRO : Method resolution order means, the constructor of class to be initialized in the child class constructor
#       will get priority on the basic of order of class being called during setup of inheritance

class Son(Father, Mother):
    """
        when we set up inheritance between two classes, then we have to initialize the parent
        class constructor inside the child class constructor with the help super keyword.

        """

    def __init__(self, son_name, f_name, f_business, m_name, m_business):
        super().__init__(f_name, f_business)
        self.mother_name = m_name
        self.mother_business = m_business
        self.son_name = son_name

    def son_details(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.father_details()
        self.mother_details()
        self.son_details()


obj = Son("Ram", "Rao", "Construction", "Kala", "Fashion")
obj.family_details()

"""
Father Name : Rao
Father Business : Construction
Mother Name : Kala
Mother Business : Fashion
Son Name : Ram
"""
