#!/usr/bin/env python3

__version__ = '1.0'
__author__  = "lippek@hva.nl"
__opgave__  = 'w3o1'

def isElem(list, element):
    """ Test whether an element `element` is in the list `list`
        return True or False
    """
    if len(list) == 0:
        return False

    for listElement in list:
        if listElement == element:
            return True
            
    return False
