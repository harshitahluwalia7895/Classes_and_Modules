class Student:

    def __init__(self):
        self.name = 'student'
        self.rno = 0

    def display(self):
        print("Name: {}, RollNo: {}, Age: {}, Marks: {}". \
              format(self.name, self.rno, self.age, self.marks))

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks
s1=Student()
s1.setAge(21)
s1.setMarks(75)
s1.display()