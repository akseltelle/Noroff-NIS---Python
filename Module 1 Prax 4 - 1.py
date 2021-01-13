# School        : Noroff - Network and IT-Security
# Author        : Aksel Telle
# Email         : akseltelle98@gmail.com
# Github        : https://github.com/akseltelle
# This project  : https://github.com/akseltelle/Noroff-NIS---Python
# Website       : https://fawdaw.com/

import os

print("Welcome " + os.getlogin())

friends = []
morefriends = []
i = 0
maxLengthList = 1
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
    morefriends = input("Do you want to add more friends? (y/n): ")
    if morefriends.lower() == "y" or morefriends.lower() == "yes":
        howmany = input("How many friends do you wish to add? ")
        maxLengthList2 = 4
        while len(morefriends) < maxLengthList2:
            i += 1
            name2 = input("Enter name %d: " %i)
            if name2 == "":
                exit("Error, name not added. Exiting")
            morefriends.append(name2)
        morefriends.sort()
    else:
        print("Not adding more friends to list.")
elif search_friends.lower() == "n" or search_friends.lower() == "no":
    exit("Not showing any friends. Exiting.")
elif search_friends.lower() == "":
    exit("Cancel Selected. Exiting.")
else:
    print("No friends shown. Exiting.")
