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