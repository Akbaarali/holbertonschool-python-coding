#!/usr/bin/python3
"""
This module defines a Square class with size validation
and an area computation method.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
