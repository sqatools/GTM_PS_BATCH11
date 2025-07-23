from account_class import account

class admin(account):
    def __init__(self, admin_head='Mr Aditya', admin_assistant='Mr Gourav Sharma'):
        super().__init__()
        self.admin_head = admin_head
        self.admin_assistant = admin_assistant

    def show_admins_details(self):
        print("Head of admin department :", self.admin_head)
        print("Assistant of admin department :", self.admin_assistant)