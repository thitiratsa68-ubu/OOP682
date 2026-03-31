#BAD IDEA: This class is trying to do too much. It should be broken down into separate classes for generating PDFs, generating Excel files, and sending emails.

class reportgenerator:
    def __init__(self, data):
        self.data = data

    def generate_pdf(self):
        pass
    
    def generate_excel(self):
        pass
    
    def send_email(self, recipient):
        pass