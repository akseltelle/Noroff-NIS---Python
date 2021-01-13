# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

class employee:
    def __init__(self, name):
        self.name = name

first = employee("Frey")
second = employee("Klaus")

setattr(first, "name", "Freya")

print(getattr(first, "name"))

delattr(second, "name")

if hasattr(second, "name"):
    print(getattr(second, "name"))
else:
    print("Second does not have attribute name")