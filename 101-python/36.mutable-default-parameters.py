from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


student = Student("Hudayfe")
student.take_exam(90)
student2 = Student("Yurt")
student2.take_exam(78)
print(student.grades)





class Student2:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


student = Student2("Hudayfe")
student.take_exam(90)
student2 = Student2("Yurt")
student2.take_exam(78)
print(student.grades)
