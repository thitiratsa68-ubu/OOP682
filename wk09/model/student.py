from .Person import Person

class Student(Person):
    def __init__(self,name,age,pid,student_id):
        super().__init__(name,age,pid)
        self.student_id = student_id
    
    def __str__(self):
        return (f'Person {self.pid} Name {self.name} age {self.age} student_id {self.student_id}')
