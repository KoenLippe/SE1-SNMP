#!/usr/bin/env python3

__version__ = '1.0'
__author__  = "lippek@hva.nl"
__opgave__  = 'w3o3'




def produceerReeks(x):
    string = ''
    string += str(x)

    if x <= 0:
        return ''

    while x != 1:
        if x % 2 == 0:
            x /= 2
            string += ',' + str(x)
        else:
            x = (x *3)+1
            string += ',' + str(x)

    return string
