import zipfile

# with zipfile.ZipFile("myarchive.zip", "r") as zipfile:
#     for current in zipfile.namelist():
#         print(current)

with zipfile.ZipFile("myarchive.zip", "r") as zipfile:
    file_info = zipfile.getinfo("A1.png")
    print("File Size: {} bytes".format(file_info.file_size))
    print("Compressed Size: {} bytes".format(file_info.compress_size))
    print("Last Modified: {} bytes".format(file_info.date_time))