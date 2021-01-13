# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

class student:
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        student.count += 1
        self.number = student.count
        self.grades = {}

    def display(self):
        print("{}:\t{} {}".format(self.number, self.name, self.surname))
        print()
        if len(self.grades) == 0:
            print("\tNo subjects and results have been added")
        else:
            for key in self.grades:
                print("\t{}:\t\t{}".format(key, self.grades[key]))

            print("\tAverage:\t{}".format(self.calculate_average()))

        print("-" * 50)

    def add_subject_and_mark(self, subject, mark):
        self.grades[subject] = mark

    def calculate_average(self):
        total = 0

        for key in self.grades:
            total += self.grades[key]

        return total / len(self.grades)

first_student = student("John", "Doe")
second_student = student("Jane", "Doe")
second_student.add_subject_and_mark("NET", 75)
second_student.add_subject_and_mark("RPG0", 90)

first_student.display()
second_student.display()

print("Numbers of stidents: {}".format(student.count))
