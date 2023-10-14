#!/usr/bin/python3

"""
this is a class square
"""


class Square():
    """ this is given its attr here """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ the attr given to the class """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.height = self.width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ what is printed out when class is printed out """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
