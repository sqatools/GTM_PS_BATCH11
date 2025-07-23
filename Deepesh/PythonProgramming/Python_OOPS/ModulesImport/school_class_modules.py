from st_module.student_class import student

class school(student):
    def __init__(self, school_head, school_assistant):
        super().__init__()
        self.school_head = school_head
        self.school_assistant = school_assistant

    def show_schools_details(self):
        print("Head of school department :", self.school_head)
        print("Assistant of school department :", self.school_assistant)



obj = school('Mr Aditya Narayan', 'Mr Shyam Raghu')
obj.show_teachers_details()
obj.show_accounts_details()
obj.show_schools_details()
obj.show_students_details()
obj.show_admins_details()