# Author: Aksel Telle
import os

print("Welcome " + os.getlogin())

friends = []
i = 0
maxLengthList = 10
while len(friends) < maxLengthList:
        i += 1
        name = input("Enter name %d: " %i)
        if name == "":
            exit("Error, name not added. Exiting")
        friends.append(name)
friends.sort()

search_friends = input("Do you want to show all friends? (y/n): ")
if search_friends.lower() == "y" or search_friends.lower() == "yes":
    print(*friends)
elif search_friends.lower() == "n" or search_friends.lower() == "no":
    exit("Not showing any friends. Exiting.")
elif search_friends.lower() == "":
    exit("Cancel Selected. Exiting.")
else:
    print("No friends shown. Exiting.")
