#!/usr/bin/env python3

__version__ = '1.0'
__author__  = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP'
__opgave__  = 'w3o1test'

from w3o1 import isElem

# Testcode, niet veranderen
# Dit test de juiste werking van isElem

# ------------------------------------------------
# I strongly disagree with the abbreviation of variables. The single letter variables are not descriptive enough.
# I have to figure out where the variables are used for, this is not necessary as this can be easily avoided by having descriptive variables names
#   __author__: Koen Lippe (500794493)
# ------------------------------------------------



if __name__ == '__main__':
    for element, list, expectedResult in [
            (1, [ 9, 4, 8 ], False),
            (8, [ 9, 8, 4 ], True),
            (7, [ 7, 7, 4 ], True),
            (5, [ 7, 7, 4, 3, 3, 1 ], False),
            (3, [], False), #ADDED BY KOEN LIPPE
        ]:
        result = isElem(list, element)
        if expectedResult == result:
            print('Correct: isElem({}, {}) --> {}'.format( # This previous description does not clearly indicate if the test has been succesful
                element, list, result))
        else:
            print('Error: isElem({}, {}) --> {} != {}'.format(
                element, list, result, expectedResult))
