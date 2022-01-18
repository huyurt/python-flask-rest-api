class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Hudayfe", (98, 83, 88, 100, 79))
student2 = Student("Yurt", (80, 92, 99, 82, 94))

print(student.average_grade())
print(student2.average_grade())
