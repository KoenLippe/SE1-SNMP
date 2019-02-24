#!/usr/bin/env python3

__version__ = '3.0'
__author__ = 'koen.lippe@hva.nl'
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
    if a == 1:
        if b == 1:
            return 0

    return 1
    # ... write your code and return 0 or 1


def myAnd(a, b):
    return myNand(myNand(a,b), myNand(a,b))
    # TODO: This code is not readable, I will edit this later

def myOr(a, b):
    return myNand(myNand(a,a), myNand(b,b))
    # TODO: This code is not readable, I will edit this later

def myNor(a, b):
    temp = myNand(myNand(a,a), myNand(b, b)) #acts as a OR gate
    return myNand(temp, temp) #Acts as a NOT gate
    # TODO: This code is not readable, I will edit this later

def myXor(a, b):
    return myNand(myNand(a, myNand(a,b)), myNand(myNand(a,b), b))
    # TODO: This code is not readable, I will edit this later

def myNot(a):
    return myNand(a,a)


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
    test1(myNot, [(0, 1), (1, 0)])
    test2(myNand, [((0, 0), 1), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)])
    test2(myAnd, [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1)])
    test2(myOr, [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)])
    test2(myNor, [((0, 0), 1), ((0, 1), 0), ((1, 0), 0), ((1, 1), 0)])
    test2(myXor, [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)])
    print('tests completed')
