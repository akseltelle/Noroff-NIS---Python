# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/
import os                                                           # Import OS module to extract system information
print("Welcome, " + os.getlogin() + "!")                            # Greet the user with a welcome message
print()
# print("Opening thefile.txt")
# my_file = open("thefile.txt", "w")
# print()
# print("Fle methods and properties")
# print("Name: ", my_file.name)
# print("Mode: ", my_file.mode)
# print("Closed: ", my_file.closed)
# print("Readable: ", my_file.readable())
# print("Writable: ", my_file.writable())
# print()
#
# # Method 1
# write_me = "This is a test\n"
# my_file.write(write_me)
#
# # Method 2
# my_file.write("Hello there!\n")
# my_file.write("Hello there!\n")
# my_file.write("Hello there!\n")
#
# print("Closing thefile.txt")
# my_file.close()
# print()
# print("Fle methods and properties")
# print("Closed: ", my_file.closed)



# my_file = open("thefile.csv", "w")
# # write_me = "This is a test"
# # my_file.write(write_me)
#
# my_file.write("Name,Description,Amount\n")
# my_file.write("John Doe,First Customer,1000.00\n")
# my_file.write("Jane Doe,Second Customer,2500.00\n")

my_file = open("thefile.csv", "r")
file_contents = my_file.readlines()
print(file_contents)
print()
for line in file_contents:
    print(line,end="")
my_file.close()
