from .Person import Person

class Staff(Person):
    def __init__(self,name,age,pid,staff_id):
        super().__init__(pid,name,age)
        self.staff_id = staff_id
    def __str__(self):
        return (f'Staff: {self.name}, Age {self.age}, Pid {self.pid}, staff_id {self.staff_id}')