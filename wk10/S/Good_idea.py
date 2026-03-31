#GOOD Idea: Separate the concerns of data processing, report generation, and email sending into different classes.

class PDFreprotgenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        pass

class excelreportgenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        pass
    
class Emailsender:
    def __init__(self, recipient):
        self.recipient = recipient

    def send_email(self):
        pass