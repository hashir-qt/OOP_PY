
class Student:
 def __init__(self, name, marks):
   self.name = name
   self.marks = marks

 def Display(self):
     print(f"{self.name} scored {self.marks} in Exams")

student1 = Student("Hashir",80)
student1.Display()
student2 = Student("Venom",70)
student2.Display()