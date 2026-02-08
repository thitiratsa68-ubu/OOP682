from wk09.model.student import Student
from wk09.model.Staff import Staff
from wk09.model.Person import Person


student_obj = Student(name="boat",age=19,pid=1234567890123,student_id=1234)
staff_obj = Staff(12345,'bob',35,'st1234')
def get_person_info(Person):       
    return f'Name: {Person.name}'

print(get_person_info(student_obj))