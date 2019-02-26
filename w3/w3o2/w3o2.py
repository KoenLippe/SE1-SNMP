#!/usr/bin/env python3

__version__ = '1.0'
__author__  = "lippek@hva.nl"
__opgave__  = 'w3o2'


def greatest(list):
    """ Find the greates element in the list """

    #List is empty so return None
    if len(list) == 0:
        return None

    #Set the first highest number to the first number in the listself.
    #This is so that negative numbers are also possible
    highest = list[0]
    for element in list:
        if element > highest:
            highest = element

    return highest
