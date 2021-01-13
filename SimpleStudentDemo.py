from SimpleStudent import *

first_student = SimpleStudent
SimpleStudent.count += 1

second_student = SimpleStudent
SimpleStudent.count += 1

print("Number of students:  {}".format(SimpleStudent.count))
