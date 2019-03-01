#!/usr/bin/env python3

__version__ = '1.0'
__author__  = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP'
__opgave__  = 'w3o1test'

from w3o4 import fibonacci


if __name__ == '__main__':

    for i, expectedResult in [
            ( 1, 1),
            ( 2, 1),
            ( 3, 2),
            ( 4, 3),
            ( 5, 5),
            ( 6, 8),
            ( 7, 13),
            ( 8, 21),
            ( 9, 34),
            (35, 9227465),
        ]:
        result = fibonacci(i)
        if expectedResult == result:
            print('fibonacci({}) --> {}'.format(
                i, result))
        else:
            print('Error:fibonacci({}) --> {} != {}'.format(
                i, result, expectedResult))
