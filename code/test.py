class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg(self):
        return round(sum(self.grades) / len(self.grades), 2)

student1 = Student("Mihir",[89, 92, 84])

student2 = Student("Ashish", [67, 72, 76])

print(student1.name, student1.grades, student1.avg())
print(student2.name, student2.grades, student2.avg())