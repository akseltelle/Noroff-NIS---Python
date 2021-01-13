# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

# repeat_me = "This string will repeat | "
# new_string = repeat_me * 3
# print(new_string)
# print()
#
# new_string = " | " + repeat_me * 3
# print(new_string)
# print()
#
# def my_test_function():
#     '''This is a test function'''
#     return
#
# print(my_test_function.__doc__)
#
# test_string = "This is my string"
# slice_of_test_string = test_string[3]
# print("test_string: ", test_string)
# print("slice at index 3: ", slice_of_test_string)
#
#
# test_string = "This is my string"
#
# print("Membership inclusive:")
# print("This" in test_string)
# print("John" in test_string)
#
# print("Membership exclusive:")
# print("This" not in test_string)
# print("John" not in test_string)
#
#
# print("This is a \t string")  # normal behaviour
# print(r"This is a \t string")  # Interpretend as a raw string




#Slide 1
# tab_variable = 'this is a \t space'
# print(tab_variable)
#
# string_with_quotations = "\I\'m a developer\\"
# print(string_with_quotations)
#
# string_1 = "one"
# string_2 = "two"
# concat_string = string_1 + string_2
# print(concat_string)
#
# repeat_me = "I want to be repeated 5 times | "
# print_repeat = repeat_me * 5
# print(print_repeat)

#Slide 2
# slice_my_string = "This is my string"
# print(slice_my_string[5])
# print("slice at index 1 up to index 10, step 2: ", slice_my_string[1:10:2])
#
# look_for_aksel = "Is Aksel here?"
# print("Alex" in look_for_aksel)
# print("Aksel" in look_for_aksel)
#
# def my_test_function():
#     '''This is a function to demonstrate the use of a docstring'''
#     return
# print(my_test_function.__doc__)




# my_string = "{} sold {} items."
# print(my_string.format("Olaf",20))
#
# print("This example requires {} argument(s).".format(1))
#
# my_string = "{0} sold {1} items. {2} sold {3} items. {2} was a better salesperson than {0}."
#
# first_person = "Olaf"
# second_person = "Nina"
# first_sales = 10
# second_sales = 20
#
# print(my_string.format(first_person, first_sales, second_person, second_sales))


# print("f: {0:f}".format(50.4756))
# print(".2f: {0:.2f}".format(50.4756))
# print(".6f: {0:.6f}".format(50.4756))
# print("e: {0:e}".format(50.4756))
# print("b: {0:b}".format(231))
# print("o: {0:o}".format(231))
# print("x: {0:x}".format(231))
# print("X: {0:X}".format(231))


#PRAX
# my_string = "{} ate {} ice creams."
# print(my_string.format("I", 100))
#
# my_indexed_string = "{0} went to the shop and bought {1} {2}, then walked to {3} and had sex for {4} hours."
# # me = "I"
# # cola = 5
# # walk = "park"
# me = input("Who are you? ")
# item = input("What did you buy? ")
# amount = input("How many did you buy? ")
# walk = input("Where did you go after? ")
# hours = input("For how long? ")
#
#
# # print(my_indexed_string.format(me, cola, walk))
# print(my_indexed_string.format(me, item, amount, walk, hours))

# the_string = "a king, named George, fell into the gorge."
#
# print("capitalize(): ", the_string.capitalize())
# print("title(): ", the_string.title())
# print("upper(): ", the_string.upper())
# print("lower(): ", the_string.lower())
# print("swapcase(): ", the_string.swapcase())

# seperator_one = ";"
# seperator_two = ","
# seperator_three = "###"
#
# the_list = ["1", "2", "3", "4"]
#
# print(";   :", seperator_one.join(the_list))
# print(",   :", seperator_two.join(the_list))
# print("### :", seperator_three.join(the_list))


# input_string = "this is the string to split"
#
# result_one = input_string.split()
# print("Default split (on spaces):")
# print(result_one)
# print()
# result_two = input_string.split("i")
# print("Split on i:")
# print(result_two)
# print()
# result_three = input_string.split("is")
# print("Split on is:")
# print(result_three)

# input_string = "    a string with horizontal whitespace    "
# print(input_string)
#
# print("lstrip(): ", input_string.lstrip())
#
# print("rstrip(): ", input_string.rstrip())
#
# print("strip(): ", input_string.strip())


# input_string = ("Dear RECIPIENT, Please find attached a cheque to the amount of AMOUNT. Kind regards, SENDER")
#
# input_string = input_string.replace("RECIPIENT", "Jhon")
# input_string = input_string.replace("AMOUNT", "3000.000 NOK")
# input_string = input_string.replace("SENDER", "Management")
#
# print(input_string)


# description_one = "Description 1"
# description_two = "Description 2"
# price_one = "3456.89"
# price_two = "563.45"
# print(description_one.ljust(20, " "), price_one.rjust(10, " "), sep="")
# print(description_two.ljust(20, " "), price_two.rjust(10, " "), sep="")
# print()
#
# print(description_one.rjust(20, " "), price_one.rjust(10, " "), sep="")
# print(description_two.rjust(20, " "), price_two.rjust(10, " "), sep="")
# print()
#
# print(description_one.ljust(20, "."), price_one.rjust(10, "."), sep="")
# print(description_two.ljust(20, "."), price_two.rjust(10, "."), sep="")
# print()
#
# print(description_one.center(20, "-"), price_one.center(10, "-"), sep="")
# print(description_two.center(20, "-"), price_two.center(10, "-"), sep="")
# print()


