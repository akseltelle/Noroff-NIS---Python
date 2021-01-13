class employees:
    count = 0

    def __init__(self):
        self.name = ""
        self.surname = ""
        employees.count += 1
        self.number = employees.count

first_employee = employees()
first_employee.name = "Leonard"
first_employee.surname = "Hofsteder"

second_employee = employees()
second_employee.name = "Sheldon"
second_employee.surname = "Cooper"

third_employee = employees()
third_employee.name = "Amy"
third_employee.surname = "Farafowler"

print("{}: {} {}".format(first_employee.number, first_employee.name, first_employee.surname))
print("{}: {} {}".format(second_employee.number, second_employee.name, second_employee.surname))
print("{}: {} {}".format(third_employee.number, third_employee.name, third_employee.surname))
print("Number of students: {}".format(employees.count))