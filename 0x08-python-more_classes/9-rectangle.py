#!/usr/bin/python3
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        result = ''
        for i in range(self.height):
            result += '#' * self.width
            if i < self.height - 1:
                result += '\n'
        result += '\nBye rectangle...'
        return result

    @classmethod
    def square(cls, size):
        return cls(size, size)
