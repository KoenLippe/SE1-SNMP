#!/usr/bin/env python3

__version__ = '1.0'
__author__ = 'student@hva.nl'
__opgave__ = 'w1o3.py'

# Implementeer myNand en definieer myAnd, myOr, myXor, myAnd and myNot met myNand.

def myNand(a, b):
    """ Nand-functie: returns de result of nand(a, b)
        Uses if statements
    Arguments
        a: 0 of 1
        b: 0 of 1
    Result
        r: 0 of 1
    """
    # ... write your code and return 0 or 1
    return 0

def myAnd(a, b):
    # ... write your code and return 0 or 1
    return 0

def myOr(a, b):
    # ... write your code and return 0 or 1
    return 0

def myNor(a, b):
    # ... write your code and return 0 or 1
    return 0

def myXor(a, b):
    # ... write your code and return 0 or 1
    return 0

def myNot(a):
    # ... write your code and return 0 or 1
    return 0

def test1(opr, testSet):
    """ Test operator with one argument
        Arguments
        opr:    function to test
        testSet:list of arg, res
    """
    for a, r in testSet:
        rr = opr(a)
        if rr != r:
            print('Error: {0:s}({1:d}): {2:d} != {3:d}'.format(
                    opr.__name__, a, r, rr))

def test2(opr, testSet):
    """ Test operator with two arguments
        Arguments
        opr:    function to test
        testSet:list of args, res
    """
    for (a, b), r in testSet:
        rr = opr(a, b)
        if rr != r:
            print('Error: {0:s}({1:d}, {2:d}): {3:d} != {4:d}'.format(
                opr.__name__, a, b, r, rr))


# Test your code !!
if __name__ == '__main__':
    test1(myNot,   [(0, 1), (1, 0) ])
    test2(myNand,  [((0, 0), 1), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0) ])
    test2(myAnd,   [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1) ])
    test2(myOr,    [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1) ])
    test2(myNor,   [((0, 0), 1), ((0, 1), 0), ((1, 0), 0), ((1, 1), 0) ])
    test2(myXor,   [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0) ])
    print('tests completed')


