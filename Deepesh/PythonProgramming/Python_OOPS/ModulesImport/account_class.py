

class account:
    def __init__(self, account_head='Mr Rahul Gupta', account_assistant='Mr Manish Verma'):
        self.account_head = account_head
        self.account_assistant = account_assistant

    def show_accounts_details(self):
        print("Head of account department :", self.account_head)
        print("Assistant of account department :", self.account_assistant)