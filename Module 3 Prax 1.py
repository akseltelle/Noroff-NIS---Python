# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

import os                                                           # Import OS module to extract system information
print("Welcome, " + os.getlogin() + "!")                            # Greet the user with a welcome message
print("")
print("(Type \"ex\" for example sentence)")                         # Give the user an example message
print("(Type \"e\" to exit program)")                               # Give the user an option to exit
user_string = input("Please enter a sentence: ")                    # Ask user for a sentence
if user_string == "ex":                                             # If user select example sentence
    conv_string = "    This is an EXAMPLE sentence.    "
elif user_string == "e":                                            # If user want to exit
    exit("Program exited")                                          # "e" selected, exit program
else:                                                               # If the user type their own sentence
    conv_string = user_string
print("\n")
print("Your sentence is \"" + conv_string + "\"")                   # Print user's message
print("")
print("Options:")                                                   # View menu to user
print("****************************************")
print("Uppercase                          :   1")
print("Lowercase                          :   2")
print("Titlecase                          :   3")
print("Remove front and back whitespaces  :   4")
print("Exit program                       :   e")
print("")
user_menu = input("What do you want to do? ")                       # Ask user what they want to do
print("")
if user_menu == "1":                                                # "1" selected, print sentence in uppercase
    print(conv_string.upper())
elif user_menu == "2":                                              # "2" selected, print sentence in lowercase
    print(conv_string.lower())
elif user_menu == "3":                                              # "3" selected, print sentence in titlecase
    print(conv_string.title())
elif user_menu == "4":                                              # "4" selected, print sentence without whitespaces
    print(conv_string.strip())
else:
    exit("Program exited")                                          # "e" selected, exit program
