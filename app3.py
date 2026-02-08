from wk09.model.classroom import Classroom
from wk09.model.student import Student

oop = Classroom("oop")
oop.addstudent(Student("Boat", 50, 1, "2001"))
oop.addstudent(Student("tingnong", 67, 2, "jokhed"))
print(f"จำนวนนักศึกษาที่ลงทะเบีบน {len(oop)}")
oop.addstudent(Student("สะแตง", 25, 3, "5555"))
print(f"จำนวนนักศึกษาที่ลงทะเบีบน {len(oop)}")
print("Students in the class : ")
for i in range(len(oop)):
    print(oop[i])