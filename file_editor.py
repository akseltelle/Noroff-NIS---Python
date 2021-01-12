import pickle
import os
import requests

print("************************************")
print("*      Welcome to File Editor      *")
print("************************************")
print("*                                  *")
print("* Create a file................. 1 *")
print("* Delete a file................. 2 *")
print("* Open a file................... 3 *")
print("* See if a file exist........... 4 *")
print("*                                  *")
print("************************************")
usermenu = input("What do you want to do? ")
if usermenu == "1":
    print("Creating a new file")
    create_filename = input("Filename: ")
    if os.path.isfile(create_filename):
        print("\n")
        print("*       File already exist!        *")
        print("************************************")
        print("*                                  *")
        print("* Overwrite..................... 1 *")
        print("* Cancel........................ 2 *")
        print("*                                  *")
        print("************************************")
        create_filename_exist = input("What do you want to do? ")
        if create_filename_exist == "1":
            print(create_filename + " has been removed. Creating new file...")
            os.remove(create_filename)
        elif create_filename_exist == "2":
            exit("Canceled")
    else:
        create_filename_content = input("File content: ")
        create_filename_create = open(create_filename, "w")
        create_filename_create.write(create_filename_content)
        print("File " + create_filename + " has been created!")
    print("\n")
elif usermenu == "2":
    print("Delete a file")
    delete_filename = input("Filename: ")
    if os.path.isfile(delete_filename):
        delete_filename_confirm = input("Are you sure that you want to delete " + delete_filename + "? (y/n) ")
        if delete_filename_confirm == "y":
            if delete_filename == "file_editor.py":
                exit("You are trying to delete a file that is required to run this program. Canceled!")
            else:
                os.remove(delete_filename)
                print("File " + delete_filename + " has been deleted!")
        elif delete_filename_confirm == "n":
            exit("Canceled. File not deleted")
        else:
            exit("No selection was made")
    else:
        print("File " + delete_filename + " does not exist, and can not be deleted")
elif usermenu == "3":
    print("Open a file")
    open_filename = input("Filename: ")
    if os.path.isfile(open_filename):
        open_filename_run = open(open_filename, "r")
        open_filename_contents = open_filename_run.readlines()
        print()
        for line in open_filename_contents:
            print(line, end="")
        open_filename_run.close()
        print()
    else:
        print("File " + open_filename + " does not exist, and can not be deleted")
elif usermenu == "4":
    print("See if a file exist")
    check_filename = input("Filename: ")
    if os.path.isfile(check_filename):
        print("The file " + check_filename + " exist!")
    else:
        print("The file " + check_filename + " does not exist!")
