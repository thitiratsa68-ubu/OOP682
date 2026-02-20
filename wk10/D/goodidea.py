from abc import ABC, abstractmethod

class Database(ABC): # Abstract Base ckass
    @abstractmethod
    def save(self):
        pass
    
class MySQLDatabaseConnection(Database):
    def save(self, data):
        print("Saving data to MySQL database")
        
class PostgreSQLDatabaseConnection(Database):
    def save(self, data):
        print("Saving data to PostgreSQL database")

class App:
    def __init__(self, database: Database):
        #App พึ่งพาอาศัย Database interface แทนที่จะพึ่งพา MySQLDatabaseConnection โดยตรง
        self.database = database
        
    
    def save_data(self, data):
        self.database.save(data)

#GOOD IDEA: The App class is decoupled from specific database implementations. We can easily switch databases by passing a different Database instance.