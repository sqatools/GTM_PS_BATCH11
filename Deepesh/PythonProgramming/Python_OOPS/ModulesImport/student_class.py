from teacher_class import teacher

class student(teacher):
    def __init__(self, student_head='Mohan', student_assistant='Ravi'):
        super(student, self).__init__()
        self.student_head = student_head
        self.student_assistant = student_assistant

    def show_students_details(self):
        print("Head of student department :", self.student_head)
        print("Assistant of student department :", self.student_assistant)