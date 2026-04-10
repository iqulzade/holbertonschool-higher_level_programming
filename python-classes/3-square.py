#!/usr/bin/python3
"""This module defines a Square class with size validation and area."""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes the square with a validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
