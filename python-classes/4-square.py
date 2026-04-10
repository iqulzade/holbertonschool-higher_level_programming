#!/usr/bin/python3
"""This module defines a Square class with size property and area calculation."""


class Square:
    """Represents a square with controlled access to size."""

    def __init__(self, size=0):
        """Initializes the square using the size setter.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
