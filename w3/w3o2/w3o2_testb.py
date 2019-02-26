#!/usr/bin/env python3

__version__ = '1.0'
__author__  = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP'
__opgave__  = 'w3o2_testb'

from w3o2 import greatest

# Testcode, niet veranderen
# Dit test de juiste werking van isElem
if __name__ == '__main__':
    for l, r in [
            ([ 9, 4, 8 ], 9),
            ([ 9, 8, 4 ], 9),
            ([ 7, 7, 4 ], 7),
            ([ 7, 7, 4, 3, 3, 1 ], 7),
            ([ -1, -2, -6, -4 ], -1),
        ]:
        res = greatest(l)
        if r == res:
            print('Suuces: greatest({}) --> {}'.format(
                l, res))
        else:
            print('Error:greatest({}) --> {} != {}'.format(
                l, res, r))
