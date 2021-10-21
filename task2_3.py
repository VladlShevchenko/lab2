class Student:
    surnames = []
    names = []
    def __new__(cls, name, surname, book, *grades):
        if surname in cls.surnames and name == cls.names[cls.surnames.index(surname)]:
                return None
        return super(Student, cls).__new__(cls)

    def __init__(self, name, surname, bookNumber, *grades):
        if not isinstance(surname, str) :
            raise TypeError("Wrong type of surname!")
        if not surname.isalpha() :
            raise ValueError("Wrong value of surname!")
        self.surname = surname
        if not isinstance(name, str) :
            raise TypeError("Wrong type of name!")
        if not name.isalpha():
            raise ValueError("Wrong value of name!")
        self.name = name
        if not isinstance(bookNumber, int) :
            raise TypeError("Wrong type of bookNumber!")
        if bookNumber <= 0:
            raise ValueError("Wrong value of bookNumber!")
        self.bookNumber = bookNumber
        for grade in grades:
            if not isinstance(grade, int):
                raise TypeError("Wrong type of grades") 
        for grade in grades:
            if grade <= 0:
                raise ValueError("Wrong value of grades")
        self.grades = grades

        self.average = 0
        self.averagePoint()
        Student.names.append(name)
        Student.surnames.append(surname)
    def averagePoint(self):
        self.average = sum(self.grades)/len(self.grades)

class Group:
    averagePointsRate = []
    def __init__(self, students):
        for student in students:
            if not isinstance(student, Student):
                raise TypeError("Wrong type of student!")
        self.students = students

    def formRate(self):
        """"A function that finds the 5 students with the best score"""
        averagePoints = []
        for student in self.students:
            averagePoints.append(student.average)
        averagePoints.sort()
        averagePoints.reverse()

        i=0
        while i < 5:
            for student in self.students:
                if averagePoints[i] == student.average:
                    self.averagePointsRate.append(f'{student.name}{student.surname} {student.average}\n')
        i += 1

    def getRate(self):
        """"A function that returns the 5 students with the best score"""
        return ''.join(self.averagePointsRate)

student1 = Student("Shevchenko", "Vladyslav", 100, 10, 11, 12)
student2 = Student("Some", "Student", 322, 12, 10, 8)
student3 = Student("Sasha", "Perfectjob", 345, 10, 12, 12)
student4 = Student("Student", "Name", 305, 10, 12, 12)
student5 = Student("Surname", "Ira", 635, 5, 12, 11)
student6 = Student("Job", "Perfect", 325, 4, 12, 11)
student7 = Student("Some", "StudentFiot", 111, 11, 11, 11) 
student8 = Student("Some", "StudentTef", 235, 9, 12, 11) 

group = [student1, student2, student3, student4, student5, student6, student7, student8]
for i in group:
    if not i:
        del group[group.index(i)]

Group = Group(group)
Group.formRate()
print(Group.getRate())
