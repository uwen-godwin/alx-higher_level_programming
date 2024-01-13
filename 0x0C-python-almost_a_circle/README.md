# Project Title: Python - Almost a Circle

## Overview
This project focuses on creating classes for geometric shapes (Rectangles and Squares) with additional features such as serialization, unit testing, and file I/O.

## Table of Contents
- [General](#general)
- [Unit Testing](#unit-testing)
- [Serialization and Deserialization](#serialization-and-deserialization)
- [Named Arguments](#named-arguments)
- [Requirements](#requirements)
- [Code Styling](#code-styling)
- [Directory Structure](#directory-structure)
- [Tasks](#tasks)

## General
This section provides a brief introduction to the project, highlighting its main goals and features.

### Unit Testing
Unit testing is implemented using the `unittest` module. All classes and methods are thoroughly tested to ensure functionality and adherence to PEP 8 standards.

### Serialization and Deserialization
This section explains the methods for serializing and deserializing objects, using JSON files for storage.

#### Serialization
- `to_json_string(list_dictionaries)`: Convert a list of dictionaries to a JSON string.
- `to_dictionary()`: Convert an instance to a dictionary representation.

#### Deserialization
- `from_json_string(json_string)`: Convert a JSON string to a list of dictionaries.
- `create(**dictionary)`: Create an instance from a dictionary.

### Named Arguments
The project extensively uses named arguments in functions and methods, making the code more readable and self-explanatory.

### Requirements
- Python 3.8.5
- Editors: vi, vim, emacs
- All files must end with a new line
- The first line of all files should be `#!/usr/bin/python3`

### Code Styling
The code adheres to PEP 8 standards and is formatted using `pycodestyle` version 2.8.

### Directory Structure
alx-higher_level_programming
- |-- 0x0C-python-almost_a_circle
- | |-- models
- | |-- init.py
- | |-- base.py
- | |-- rectangle.py
- | |-- square.py
- |-- tests


## Tasks
This section lists the tasks associated with the project along with brief descriptions.

### 0. If it's not tested, it doesn't work
Ensure comprehensive unit tests for all files, classes, and methods. Run tests using:
```bash
python3 -m unittest discover tests
1. Base class
Create a Base class managing the id attribute for all future classes.
2. First Rectangle
Create a Rectangle class that inherits from Base and manages width, height, x, y.
3. Validate attributes
Add validation to setter methods in the Rectangle class.
4. Area first
Add a method area() to calculate the area of a Rectangle instance.
5. Display #0
Add a method display() to print the Rectangle instance using '#'.
6. str
Implement the __str__ method to return a string representation of the Rectangle instance.
7. Display #1
Update the display() method to support x and y parameters for indentation.
8. Update #0
Add an update(*args, **kwargs) method to update the attributes of the Rectangle instance.
... (Continue with the rest of the tasks)

## Conclusion
Conclude with any final thoughts, acknowledgments, or additional information.
