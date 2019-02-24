#!/usr/bin/env python3

__version__ = '1.0'
__author__  = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP & Koen Lippe (500794493)'
__opgave__  = 'w2o3'

from w2_lib import *
from w2o1 import *
from w2o2 import *

class HalfAdder(Circuit):
    """ Implement a half-adder circuit on Bits """
    def __init__(self, iBitA, iBitB, oBitS, oBitC):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitS   -- Output S (Reg, uninitialized) Sum
            oBitC   -- Output C (Reg, uninitialized) Carry
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitS, Bit) and isinstance(oBitC, Bit)

        Circuit.__init__(self)

        self.add(XorCircuit(iBitA, iBitB, oBitS))
        self.add(AndCircuit(iBitA, iBitB, oBitC))




class FullAdder(Circuit):
    """ Implement a full-adder circuit on Bits """
    def __init__(self, iBitA, iBitB, iBitC, oBitS, oBitC):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            iBitC   -- Input  C (Bit, initialized)   Carry
            oBitS   -- Output S (Reg, uninitialized) Sum
            oBitC   -- Output C (Reg, uninitialized) Carry
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit) and isinstance(oBitC, Bit)
        assert isinstance(oBitS, Bit) and isinstance(oBitC, Bit)

        Circuit.__init__(self)

        tempBit1 = Bit(name="tempBit1")
        self.add(XorCircuit(iBitA, iBitB,  tempBit1))

        self.add(XorCircuit(tempBit1, iBitC, oBitS))

        tempBit2 = Bit(name='tempBit2')
        self.add(And(iBitC, tempBit1, tempBit2))

        tempBit4 = Bit(name='tempBit4')
        self.add(And(iBitA, iBitB, tempBit4))

        self.add(Or(tempBit2, tempBit4, oBitC))
        # ... write your code

if __name__ == '__main__':
    tests = [
       # a  b  s  c
        (0, 0, 0, 0),
# Complete the test-set
        (1, 1, 0, 1),
        (1, 0, 1, 0)
        # (1, 1, 0, 1)
    ]
    for iA, iB, oS, oC in tests:
        bitIa = Bit(iA, name='iA')
        bitIb = Bit(iB, name='iB')

        bitOs = Bit(name='oS')
        bitOc = Bit(name='oC')
        c = Circuit()
        c.add(HalfAdder(bitIa, bitIb, bitOs, bitOc))
        c.run()
        if int(bitOs) != oS or int(bitOc) != oC:
            print('Error: {} + {} = s={}, c={} != s={}, c={}'.format(
                str(bitIa), str(bitIb), int(bitOs), int(bitOc),
                oS, oC))

    tests = [
       # a  b  c  s  c
        (0, 0, 0, 0, 0),
        # (1, 2, 0, 3, 0),
# Complete the test-set
        (1, 1, 1, 1, 1),
    ]
    for iA, iB, iC, oS, oC in tests:
        bitIa = Bit(iA, name='iA')
        bitIb = Bit(iB, name='iB')
        bitIc = Bit(iC, name='iC')

        bitOs = Bit(name='oS')
        bitOc = Bit(name='oC')
        c = Circuit()
        c.add(FullAdder(bitIa, bitIb, bitIc, bitOs, bitOc))
        c.run()
        if int(bitOs) != oS or int(bitOc) != oC:
            print('Error: {} + {} + {} = s={}, c={} != s={}, c={}'.format(
                str(bitIa), str(bitIb), str(bitIc), int(bitOs), int(bitOc),
                oS, oC))
    print('Tests done')

