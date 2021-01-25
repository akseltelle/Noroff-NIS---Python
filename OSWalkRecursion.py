import os

def contents(current_path):
    print(current_path[len(root_path) -5:])

    for current, subdirectories, files in os.walk(current_path):
        subdirectories.sort()
        files.sort()
        for current_subdir in subdirectories:
            next_path = os.path.join(current_path, current_subdir)
            if os.path.exists(next_path):
                contents(next_path)
        for current_file in files:
            full_file_path = os.path.join(current_path, current_file)
            if os.path.exist(full_file_path):
                print(full_file_path[len(root_path) - 5:])

root_path = os.getcwd() + "/test"
contents(root_path)
