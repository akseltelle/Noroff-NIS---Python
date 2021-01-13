# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

import sys

# help()

# print("\n")
#
#
# import keyword
#
# print("Python Keywords:")
# for theword in keyword.kwlist:
#     print(theword, end=", ") # kwlist contains a list of Python keywords
# print()
#     # iskeyword returns True or False depending on whether the word is a keyword
# print("Noroff is a Python keyword: ", keyword.iskeyword("Noroff"))
#
# print("\n")
#
# print("Python Keywords:")
# for thewordnis in keyword.kwlist:
#     print(thewordnis, end=(", "))
# print()
# print("NIS is awesome, but not a keyword in Python: ", keyword.iskeyword("NIS"))
#
# print("\n")


# import math
#
# # Declare values
# int_value = 2
# second_value = 25
# decimal_value = 5.3
#
# print("ceiling:", math.ceil(decimal_value))
#
# print("\n")


# import random
#
# print("Random number in the range 2 to 3:", random.random())
# print("Random number in the range 1 to 20:", random.random() * 100)
#
# print("\n")
# print("Select 6 random numbers: ")
# # Chooses 4 non-repeating numbers in the range 1 to 50
# print("Your random numbers are ", random.sample(range(1, 51),4))
#
# print("\n")
# print("Random number between 1 to 20, multiplied by 2:", random.randrange(1, 20) * 2)


# # Calculating decimals
# value_one = 0.7
# value_two = 1.05
# first_result = value_one * value_two
# second_result = value_one + value_two
#
# # Display the numbers with 2 floating point digits
# print("Value one: ", "%.2f" % value_one)
# print("Value two: ", "%.2f" % value_two)
# print("First result: ", "%.2f" % first_result)
# print("Second result: ", "%.2f" % second_result)
#
# # Display the numbers with 20 floating point digits
# print("Value one: ", "%.20f" % value_one)
# print("Value two: ", "%.20f" % value_two)
# print("First result: ", "%.20f" % first_result)
# print("Second result: ", "%.20f" % second_result)
#
# # Display the numbers with 50 floating point digits
# print("Value one: ", "%.50f" % value_one)
# print("Value two: ", "%.50f" % value_two)
# print("First result: ", "%.50f" % first_result)
# print("Second result: ", "%.50f" % second_result)
#
#
# import decimal
#
# value_one = 0.7
# value_two = 1.05
#
# # Display the numbers with 2 floating point digits
# print("First Number: ", "%.2f" % value_one)
# print("Second Number: ", "%.2f" % value_two)
# print("First result: ", "%.2f" % first_result)
# print("Second result: ", "%.2f" % second_result)



# from datetime import *
#
# now = datetime.today()
# print("Today: ", now)
# print("Current time: ", now.hour, ":", now.minute, ":", now.second, sep="")
# print("Current date: ", now.day, ".", now.month, ".", now.year,  sep="")
# print("Current date: ", now.day, " ", now.strftime("%B"), " ", now.year,  sep="")
# print("Current date:", now.day, now.strftime("%B"), now.year,  sep=" ")
# print("Current date and time: ", now.day, " ", now.strftime("%B"), " ", now.year, " ", now.hour, ":", now.minute, ":", now.second,  sep="")
# print("Today is a ", now.strftime("%A"), sep="")
# print("The month is ", now.strftime("%B"), sep="")

# print("\n")


from time import *

start = time()
start_time = localtime(start)
print("Started at: ",
strftime("%X", start_time))

for i in range(0,5):
    print(i + 1)
    sleep(1) # Pauses for a second

end = time()
difference = end - start
print("The loop ran for ", difference, "seconds.")
