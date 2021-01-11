# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/
print("Welcome!")
user_string = input("Please enter a sentence (type \"ex\" for example sentence): ")
if user_string == "ex":
    conv_string = "    This is an EXAMPLE sentence.    "
else:
    conv_string = user_string
print("\n")
print("Your sentence is \"" + conv_string + "\"")
print("")
print("Options:")
print("****************************************")
print("Uppercase                          :   1")
print("Lowercase                          :   2")
print("Titlecase                          :   3")
print("Remove front and back whitespaces  :   4")
print("Exit program                       :   e")
print("")
user_menu = input("What do you want to do? ")
print("")
if user_menu == "1":
    print(conv_string.upper())
elif user_menu == "2":
    print(conv_string.lower())
elif user_menu == "3":
    print(conv_string.title())
elif user_menu == "4":
    print(conv_string.strip())
else:
    exit("Program exited")
