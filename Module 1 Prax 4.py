#Source: Nils
#!/usr/bin/env python3
import os

print("Welcome " + os.getlogin())

friends = []
i = 0
maxLengthList = 3
while len(friends) < maxLengthList:
        i += 1
        name = input("Enter name %d: " %i)
        if name == "":
            exit("Error, name not added. Exiting")
        friends.append(name)
friends.sort()

search_list = input("Would you like to search for a name? Y/n/show all: ")
if search_list.lower() == "y" or search_list.lower() == "yes":
    search = input("Enter name to search for: ")
    if search in friends:
        print("Friend is found")
elif search_list.lower() == "n" or search_list.lower() == "no":
    exit("Not searching, exiting.")
elif search_list.lower() == "a" or search_list.lower() == "all" or search_list.lower() == "s" or search_list.lower() == "show" or search_list.lower() == "show all":
    print(*friends)
else:
    print("Friend is not found")
