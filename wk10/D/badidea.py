class app:
    def __init__(self,name):
        self.data = MySQLDatabaseConnection()
    def save_data(self, data):
        self.database.save(data)
    
class MySQLDatabaseConnection:
    def save(self, data):
        pass

app = app()
app.save_data("some data")
#BAD IDEA: The app class is tightly coupled with MySQLDatabaseConnection. If we want to change the database type, we would need to modify the app class.