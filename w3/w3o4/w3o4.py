#!/usr/bin/env python3

__version__ = '1.0'
__author__  = "lippek@hva.nl"
__opgave__  = 'w3o4'

def fibonacci(n):

    number1 = 1
    number2 = 0
    newNumber = 0

    for i in range(n):
        if n == 1:
            #Only first number is known (=1). This means that the return number must be 1.
            # The second number must be 1 too to continue the serie
            newNumber = number1
            number2 = number1
        else:
            #the newNumber is calculated via f(n) = f(n-1)+f(n-2)
            newNumber = number1 + number2

            #the other numbers are shifted 1 place
            number1 = number2
            number2 = newNumber

    return newNumber
