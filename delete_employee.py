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
