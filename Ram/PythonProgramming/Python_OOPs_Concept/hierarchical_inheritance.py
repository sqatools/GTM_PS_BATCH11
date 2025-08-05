# Hierarchical inheritance

class Father:
    def __init__(self, f_name, f_business):
        self.father_name = f_name
        self.father_business = f_business

    def father_details(self):
        print("Father Name :", self.father_name)
        print("Father Business :", self.father_business)


# child/derived class
class Son1(Father):

    def __init__(self, son_name, f_name, f_business):
        super().__init__(f_name, f_business)
        self.son_name = son_name

    def son_details(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.father_details()
        self.son_details()


obj = Son1("Ram", "Rao", "Construction")
obj.family_details()
"""
Father Name : Rao
Father Business : Construction
Son Name : Ram
"""

class Son2(Father):

    def __init__(self, son_name, f_name, f_business):
        super().__init__(f_name, f_business)
        self.son_name = son_name

    def son_details(self):
        print("Son Name :", self.son_name)

    def family_details(self):
        self.father_details()
        self.son_details()

print("_"*50)
obj2 = Son2("Sai", "Rao", "Construction")
obj2.family_details()

"""
Father Name : Rao
Father Business : Construction
Son Name : Sai
"""


