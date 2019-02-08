#!/usr/bin/env python3

__version__ = '1.0'
__author__ = 'koen.lippe@hva.nl'
__name__ = 'w1o1.py'


# Print "hello world" uitbreiding
def combine(arg1, arg2):
    """ Concatenates arg1 and arg2 with an space to seperate the args """
    string = arg1 + " " + arg2
    return string


# Controleer op het programma goed werkt.
# Maak zelf nog meer tests.
if __name__ == 'w1o1.py':
    print(combine("hello", "world"))
    print(combine("Koen", "Lippe"))
    print(combine("test", "123"))

    if combine("hello", "world") != "hello world":
        print("Error\n")
