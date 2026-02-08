class Person:
    def __init__(self,name,age,pid):
        self.pid = pid
        self.name = name
        self.age = age
    def __str__(self):
        return (f'Person: {self.name}, Age {self.age}, Pid {self.pid}')




