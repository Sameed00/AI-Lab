class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "D"


st1 = Student()
st2 = Student()
st3 = Student()
st1.set_marks(80)
st2.set_marks(73)
st3.set_marks(55)
print("Student 1:", st1.get_marks(), st1.calculate_grade())
print("Student 2:", st2.get_marks(), st2.calculate_grade())
print("Student 3:", st3.get_marks(), st3.calculate_grade())
     
