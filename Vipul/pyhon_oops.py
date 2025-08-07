class Student:

    city = "Dehradun"
    state = "UK"

    def __init__(self, name, roll_no):  # constructor
        self.name = name
        self.roll = roll_no   # instance variable
        print(self.name)
        print(self.roll)

    def add(self, n1, n2):
        print("addition of n1 and n2 is :", n1+n2)

    def show(self, msg):
        print("message is :", msg)

    @classmethod
    def class_method(cls):
        print("I am class method")
        print(cls.city)
        print(Student.city)

    @staticmethod
    def static_method(msg):
        print("I am static method")
        print(msg)
        v1 = 30
        print(v1)


st = Student("rahul", "55")
st.add(2,5)
st.show("I Love India")
print(st.city)
print(st.state)
Student.class_method()
Student.static_method("I am static")
# print(Student.)
