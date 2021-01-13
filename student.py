class student:
    count = 0

    def __init__(self):

        self.name = ""
        self.surname = ""
        student.count += 1
        self.number = student.count

first_student = student()
first_student.name = "John"
first_student.surname = "Doe"

second_student = student()
second_student.name = "Jane"
second_student.surname = "Doe"

third_student = student()
third_student.name = "Jack"
third_student.surname = "Jackson"

print("{}: {} {}".format(first_student.number, first_student.name, first_student.surname))
print("{}: {} {}".format(second_student.number, second_student.name, second_student.surname))
print("{}: {} {}".format(third_student.number, third_student.name, third_student.surname))
print("Number of students: {}".format(student.count))