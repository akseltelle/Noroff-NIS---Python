# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

import os                                                           # Import OS module to extract system information
print("Welcome, " + os.getlogin() + "!")                            # Greet the user with a welcome message
print()

print("Opening thefile.txt")
my_file = open("thefile.txt", "w")
print()
print("Fle methods and properties")
print("Name: ", my_file.name)
print("Mode: ", my_file.mode)
print("Closed: ", my_file.closed)
print("Readable: ", my_file.readable())
print("Writable: ", my_file.writable())
print()

# Method 1
write_me = "This is a test\n"
my_file.write(write_me)

# Method 2
my_file.write("Hello there!\n")
my_file.write("Hello there!\n")
my_file.write("Hello there!\n")

print("Closing thefile.txt")
my_file.close()
print()
print("Fle methods and properties")
print("Closed: ", my_file.closed)



my_file = open("thefile.csv", "w")
# write_me = "This is a test"
# my_file.write(write_me)

my_file.write("Name,Description,Amount\n")
my_file.write("John Doe,First Customer,1000.00\n")
my_file.write("Jane Doe,Second Customer,2500.00\n")



my_file = open("thefile.csv", "r")
file_contents = my_file.readlines()
print(file_contents)
print()
for line in file_contents:
    print(line,end="")
my_file.close()



my_file = open("thetextfile.txt", "r")
print(my_file.read())
print("Position {}".format(my_file.tell()))
print("Resetting position to 5")
my_file.seek(5)
print("Position {}".format(my_file.tell()))
print()
for line in my_file:
    print(line, end="")
my_file.close()







# Open file gag.txt
my_file = open("gag.txt", "w")

# Write a block of text with ''' '''
write_me = '''Woah! This is a large text file where i can write as much as i want!
How does spacing work?
Wonder, i must.
 Yeah Boi
'''

# Write content to file
my_file.write(write_me)

# Write a list of text 4 times
for i in range(0,4):
    my_file.write("Another line {}\n".format(i + 1))

# Open file gag.txt
my_file = open("gag.txt", "r")

# Print content in one long line
file_contents = my_file.readlines()
print(file_contents)
print()
# Print content like it was written
for line in file_contents:
    print(line,end="")

# Close file
my_file.close()






file = "myfile.txt"                         # Filename
print("Opening " + file)                    # Print opening message

my_file = open(file, "w")                   # Open file in read mode
print()
print("File methods and properties:")       # Print file information

print("Name: ", my_file.name)               # File name

print("Mode: ", my_file.mode)               # File mode

print("Closed: ", my_file.closed)           # Is file closed?

print("Readable: ", my_file.readable())     # Is file readable?

print("Writable: ", my_file.writable())     # Is file writable
print()
print("Closing " + file)                    # Print closing message

my_file.close()                             # Close file
print()
print("File methods and properties:")       # Print file information

print("Closed: ", my_file.closed)           # Is file closed?




# Write to text file
my_file = open("myfile.txt", "w")

write_me = "I am \npracticing to write\nto files.\n"
my_file.write(write_me)

# Write to CSV file
my_file = open("thecsvfile.csv", "w")
my_file.write("Name,Description,Amount\n")
my_file.write("John Doe,First Customer,1000.00\n")
my_file.write("Jane Doe,Second Customer,2500.00\n")

my_file.close()

# Reading data from files
my_file_1 = open("myfile.txt", "r")
my_file_2 = open("thecsvfile.csv", "r")

print(my_file_1.read())
print(my_file_2.read())


# Formatting
my_file = open("myfile.txt", "r")

print(my_file.read())
print("Position {}".format(my_file.tell()))
print("Resetting position to 10")
my_file.seek(10)
print("Position {}".format(my_file.tell()))
print()


# Read file
my_file = open("thecsvfile.csv", "r")

file_contents = my_file.readlines()
print(file_contents)
print()


# Append text to a file
my_file = open("thetextfile.txt", "a")

for i in range(0,40):
    my_file.write("Another line {}\n".format(i + 1))

my_file.close()


# Reading data from files
my_file_1 = open("thetextfile.txt", "r")

print(my_file_1.read())


# Create temp file
temp_file = open("temp.txt", "x")
temp_file.close()


# Remove temp file
import os
if os.path.isfile("temp.txt"):
    print("File found - removing it.")
    os.remove("temp.txt")
else:
    print("File not found - exiting.")
