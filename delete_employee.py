# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

class employee:
    def __init__(self, name):
        self.name = name

first = employee("Freya")
second = employee("Klays")
third = employee("Maia")
del second.name

print(first.name)
print(second.name)
print(third.name)
