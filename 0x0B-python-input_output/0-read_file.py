#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")

if __name__ == "__main__":
    read_file()
