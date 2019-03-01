#!/usr/bin/env python3

__version__ = '1.0'
__author__  = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP'
__opgave__  = 'w3o3test'

from w3o3 import produceerReeks

# Testcode, niet veranderen
# Dit test de juiste werking van produceerReeks
if __name__ == '__main__':
    for x, expectedResult in [
            ( 7, "7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1"),
            ( 1, "1"),
            (17, "17,52,26,13,40,20,10,5,16,8,4,2,1"),
            (13, "13,40,20,10,5,16,8,4,2,1"),
            ( 0, ""),
            (-1, ""),
        ]:
        result = produceerReeks(x)
        if expectedResult == result:
            print('Correct: produceerReeks({}) --> {}'.format(
                x, result))
        else:
            print('Error:produceerReeks({}) --> {} != {}'.format(
                x, result, expectedResult))
