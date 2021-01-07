import sys
import keyword

# help()

print("Python Keywords:")
for theword in keyword.kwlist:
    print(theword, end=", ") # kwlist contains a list of Python keywords
print()
    # iskeyword returns True or False depending on whether the word is a keyword
print("Noroff is a Python keyword: ", keyword.iskeyword("Noroff"))

print("\n")

print("Python Keywords:")
for thewordnis in keyword.kwlist:
    print(thewordnis, end=(", "))
print()
print("NIS is awesome, but not a keyword in Python: ", keyword.iskeyword("NIS"))