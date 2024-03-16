# JavaScript Objects, Scopes, and Closures

This repository contains JavaScript scripts that demonstrate various concepts related to objects, scopes, and closures.

## Tasks

1. **Rectangle #0** - Define an empty class Rectangle.
2. **Rectangle #1** - Define a class Rectangle with a constructor that initializes width and height attributes.
3. **Rectangle #2** - Modify the Rectangle class to handle cases where width or height is 0 or not a positive integer.
4. **Rectangle #3** - Add a method `print()` to the Rectangle class that prints the rectangle using the character 'X'.
5. **Rectangle #4** - Add two more methods to the Rectangle class: `rotate()` to exchange width and height, and `double()` to multiply width and height by 2.
6. **Square #0** - Define a class Square that inherits from Rectangle and initializes with a single argument for size.
7. **Square #1** - Add a method `charPrint(c)` to the Square class that prints the square using the character `c` (default to 'X').
8. **Occurrences** - Implement a function `nbOccurences(list, searchElement)` that counts occurrences of `searchElement` in `list`.
9. **Esrever** - Implement a function `esrever(list)` that reverses the given list without using the built-in method `reverse`.
10. **Log me** - Write a function `logMe(item)` that prints the number of arguments already printed and the new argument value.
11. **Number conversion** - Implement a function `converter(base)` that converts a number from base 10 to another base passed as an argument.
12. **Factor index** - Write a script that imports an array and computes a new array where each value is equal to the value of the initial list, multiplied by the index in the list.
13. **Sorted occurrences** - Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
14. **Concat files** - Write a script that concatenates two files.

## Usage

To execute any script, run it using Node.js. For example:

$ ./1-rectangle.js


## Files

- `0-rectangle.js`: Empty class Rectangle
- `1-rectangle.js`: Rectangle class with width and height attributes
- `2-rectangle.js`: Modified Rectangle class handling zero or negative values
- `3-rectangle.js`: Rectangle class with print method
- `4-rectangle.js`: Rectangle class with rotate and double methods
- `5-square.js`: Square class inheriting from Rectangle
- `6-square.js`: Square class with charPrint method
- `7-occurrences.js`: Function to count occurrences in a list
- `8-esrever.js`: Function to reverse a list
- `9-logme.js`: Function to print the number of arguments already printed
- `10-converter.js`: Function to convert numbers between bases
- `100-map.js`: Script to compute a new array with values multiplied by their index
- `101-sorted.js`: Script to compute a dictionary of user ids by occurrence
- `102-concat.js`: Script to concatenate two files
