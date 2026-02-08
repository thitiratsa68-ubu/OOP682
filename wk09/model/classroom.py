class Classroom:
    def __init__(self,name):
        self.name = name
        self.students = []

    def addstudent(self,student):
        self.students.append(student)
        return True
    
    def __len__(self):
        return len(self.students)
    
    def __getitem__(self,index):
        return self.students[index]