import os
import shutil

root_path = os.getcwd()

os.mkdir(root_path + "\\X")

##os.mkdir(root_path + "\\Y\1")

os.makedirs(root_path + "\\Y\A")

shutil.rmtree(root_path + "\\Y")

os.rmdir(root_path + "\\X")
