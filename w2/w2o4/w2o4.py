#!/usr/bin/env python3

__version__ = '1.0'
__author__  = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP & Koen Lippe 500794493'
__opgave__  = 'w2o4'

from w2_lib import *
from w2o3 import *


class Adder(Circuit):
    """ Implement a n-adder circuit """
    def __init__(self, iRegA, iRegB, oRegC, n=8):
        """
        Arguments:
            iRegA   -- Input  A (Register, initialized)
            iRegB   -- Input  B (Register, initialized)
            oRegC   -- Output C (Register, not initialized)
        Note:
            Overflow carry is ignored
            Implemented using Half- and FullAdder
        """
        assert isinstance(iRegA, Register) and isinstance(iRegB, Register)
        assert isinstance(oRegC, Register)
        assert n == len(iRegA) == len(iRegB) == len(oRegC)

        Circuit.__init__(self)


        # //Checken op


        halfAdderSum = Bit(name="HalfAdderSum")
        halfAdderCarry = Bit(name="HalfAdderCarry")

        c = Circuit()
        c.add(HalfAdder(iRegA[-1], iRegB[-1], halfAdderSum, halfAdderCarry))
        c.run()

        print(iRegA)
        print(iRegB)
        print()

        print(halfAdderSum)




        # oRegC.__setitem__(0, halfAdderSum) //Does not work. Please tell me what's wrong, syntax? :-)
        oRegC._regs[-1] = halfAdderSum



        fullAdderSum = Bit(name="FullAdderSum")
        fullAdderCarry = Bit(name="FullAdderCarry")

        fullAdderInputCarry = halfAdderCarry
        # //NUmber 26 == 11010

        # //range len(iRegA)-1 because i have already done the first calculation with a half adder
        for x in range(len(iRegA)-1):
            c = Circuit()

            # //-(x+2) because of the placement in the Register
            c.add(FullAdder(iRegA[-(x+2)], iRegB[-(x+2)], fullAdderInputCarry, fullAdderSum, fullAdderCarry))
            c.run()

            # print(fullAdderSum)

            # //Adding sum bit to the result

            oRegC._regs[-(x+2)] = fullAdderSum

            # //Setting carry input for the next loop
            fullAdderInputCarry = fullAdderCarry

        print(oRegC)


if __name__ == '__main__':
    # setVerbose(True)
    c = Circuit()
    regA = Register.fromStr(bitStr="00001101", name="A")
    regB = Register.fromStr(bitStr="00001101", name="B")
    regC = Register(n=8, name="C")
    c.add(Adder(regA, regB, regC, n=8))
    c.run()
    print('{} + {} = {}'.format(
        int(regA), int(regB), int(regC)))
    if int(regC) != 26: print('Error')

    # c = Circuit()
    # regA = Register.fromStr(bitStr="1101", name="A")
    # regB = Register.fromStr(bitStr="1101", name="B")
    # regC = Register(n=4, name="C")
    # c.add(Adder(regA, regB, regC, n=4))
    # c.run()
    # print('{} + {} = {}'.format(
    #     int(regA), int(regB), int(regC)))
    # if int(regC) != 10: print('Error')
