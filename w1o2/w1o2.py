#!/usr/bin/env python3

__version__ = '1.0'
__author__ = 'koen.lippe@hva.nl'
__name__ = 'w1o2.py'

import sys
import getopt

from w1o2_tbl import kAddTbl

def toStr(n, base=10):
    """ Convert `n` to string using `base` as base """
    assert(1 <= base <= 16)
    s = ''
    while n > 0:
        s = hex(n % base)[-1:] + s
        n = n // base
    return s.upper()

def toInt(s, base=10):
    """ Convert `s` to integer using `base` as base """
    assert(1 <= base <= 16)
    n = 0
    for i in range(0, len(s)): # i = 0, 1, ..., sLen-1
        n *= base
        n += int(s[i], base)
    return n

def myAdd(a, b, base=10):
    """ Caculate the sum of string `a` and string `b` using `base` as base """
    aLength = len(a)
    bLength = len(b)
    n = max(aLength, bLength)
    r, c = "", '0'
    for i in range(1, n+1): # i = 1, 2, ..., n
        ai = a[-i] if i <= len(a) else '0'   # Not good enough, make it better
        bi = b[-i] if i <= len(b) else '0'   # Not good enough, make it better

        # c = carry, s = sum
        c1, s1 = kAddTbl[base][c, ai]
        c2, s2 = kAddTbl[base][s1, bi]
        c = c2                                         # ... Calculate the carry using c1 and c2
        r = r + s2 if bi != '0' else r + s2 + c2    # ... Add s2 to the result string
    # Is the answer correct
    return r

gVbs = False
if __name__ == 'w1o2.py':
    opts, args = getopt.getopt(sys.argv[1:], 'V')
    for opt, arg in opts:
        if opt == '-V': gVbs = True

    tests = [
        ( "923", "77",  10 ),
        ( "724", "77",   8 ),
        ( "123", "21",   4 ),
        ( "F44", "77",  16 ),
#       ( "421", "123",  5 ), 
    ]
    for a, b, base in tests:
        c = myAdd(a, b, base)
        r = toStr(toInt(a, base) + toInt(b, base), base)
        if c != r:
            print('Error: B{}:\t{} + {} != {} [{}]'.format(base, a, b, c, r))
        else:
            print('B{}:\t{}+{}={}'.format(base, a, b, c))

        if gVbs:
            print('a={}B{} ({}), b={}B{} ({}), a+b={}B{} ({}) [{}]'.format(
                a, base, toInt(a, base), 
                b, base, toInt(b, base),
                c, base, toInt(c, base),
                toInt(a, base) + toInt(b, base)))
    print('Tests done.')
