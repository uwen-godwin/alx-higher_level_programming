import os

def add_newline_to_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "a") as file:
                file.write("\n")

your_project_directory = "/root/alx-higher_level_programming/0x08-python-more_classes/"
add_newline_to_files(0x08-python-more_classes)
