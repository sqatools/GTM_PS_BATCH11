from admin_module.admin_class import admin

class teacher(admin):
    def __init__(self, teacher_head='Mrs Pooja', teacher_assistant='Mrs Dipti'):
        super().__init__()
        self.teacher_head = teacher_head
        self.teacher_assistant = teacher_assistant

    def show_teachers_details(self):
        print("Head of teacher department :", self.teacher_head)
        print("Assistant of teacher department :", self.teacher_assistant)