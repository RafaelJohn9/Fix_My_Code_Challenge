#!/usr/bin/python3
"""
User class
"""


class User():
    """ user class method """

    @property
    def email(self):
        """ user class method """
        return self.__email

    def __init__(self):
        """ user class method """
        self.__email = None

    @email.setter
    def email(self, value):
        """ user class method """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
