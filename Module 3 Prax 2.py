# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/
import os                                                           # Import OS module to extract system information
print("Welcome, " + os.getlogin() + "!")                            # Greet the user with a welcome message
print("")
print("Opening thefile.txt")
my_file = open("thefile.txt", "w")
print("")
print("Fle methods and properties")
print("Name: ", my_file.name)
print("Mode: ", my_file.mode)
print("Closed: ", my_file.closed)
print("Readable: ", my_file.readable())
print("Writable: ", my_file.writable())
print("")

# Method 1
write_me = "This is a test\n"
my_file.write(write_me)

# Method 2
my_file.write("Hello there!\n")
my_file.write("Hello there!\n")
my_file.write("Hello there!\n")

print("Closing thefile.txt")
my_file.close()
print("")
print("Fle methods and properties")
print("Closed: ", my_file.closed)
