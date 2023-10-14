#!/usr/bin/python3
"""
module for the class square
"""


class square():
    """
    the class square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ method for attr setting """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def PermiterOfMySquare(self):
        """ Permiter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ print out of class """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
