#!/usr/bin/env python3

_version = '1.0'
__author__ = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP & Koen Lippe (500794493)'
__opgave__ = 'w2o2'

from w2_lib import *
from w2o1 import *


class NandCircuit(Circuit):
    """ Implement a And circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitQ):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitQ   -- Output Q (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitQ, Bit)

        Circuit.__init__(self)
        self.add(Nand(iBitA, iBitB, oBitQ))


class OrCircuit(Circuit):
    """ Implement a Or circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitQ):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitQ   -- Output Q (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitQ, Bit)

        Circuit.__init__(self)
        tBit1 = Bit(name='t1')
        tBit2 = Bit(name='t2')
        self.add(Nand(iBitA, iBitA, tBit1))
        self.add(Nand(iBitB, iBitB, tBit2))
        self.add(Nand(tBit1, tBit2, oBitQ))


class AndCircuit(Circuit):
    """ Implement a And circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitQ):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitQ   -- Output Q (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitQ, Bit)

        Circuit.__init__(self)

        tempBit = Bit(name='tempBit')
        self.add(Nand(iBitA, iBitB, tempBit))
        self.add(Nand(tempBit, tempBit, oBitQ))


class NorCircuit(Circuit):
    """ Implement a Nor circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitQ):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitQ   -- Output Q (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitQ, Bit)

        Circuit.__init__(self)

        tempBit1 = Bit(name='tempBit1')
        tempBit2 = Bit(name='tempBit2')
        self.add(Nand(iBitA, iBitA, tempBit1))
        self.add(Nand(iBitB, iBitB, tempBit2))

        tempBit3 = Bit(name='tempBit3')
        self.add(Nand(tempBit1, tempBit2, tempBit3))

        self.add(Nand(tempBit3, tempBit3, oBitQ))

class XorCircuit(Circuit):
    """ Implement a Xor circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitQ):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitQ   -- Output Q (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitQ, Bit)

        Circuit.__init__(self)

        tempBit1 = Bit(name="tempBit1")
        self.add(Nand(iBitA, iBitB, tempBit1))

        tempBit2 = Bit(name='tempBit2')
        tempBit3 = Bit(name='tempBit3')
        self.add(Nand(iBitA, tempBit1, tempBit2))
        self.add(Nand(iBitB, tempBit1, tempBit3))

        self.add(Nand(tempBit2, tempBit3, oBitQ))


class NotCircuit(Circuit):
    """ Implement a Not circuit using Nand-gates """
    # Please read the comment at the test set for the reason why I added oBitQ2
    def __init__(self, iBitA, oBitQ, oBitQ2):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            oBitQ   -- Output Q (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit)
        assert isinstance(oBitQ, Bit)

        Circuit.__init__(self)

        self.add(Nand(iBitA, iBitA, oBitQ2))


if __name__ == '__main__':
#   setVerbose(True)

    # Make your own test for And, Nor, Xor, Not
    tests = [
        ( NandCircuit, 0, 0, 1 ),
        ( NandCircuit, 0, 1, 1 ),
        ( NandCircuit, 1, 0, 1 ),
        ( NandCircuit, 1, 1, 0 ),

        ( OrCircuit,   0, 0, 0 ),
        ( OrCircuit,   0, 1, 1 ),
        ( OrCircuit,   1, 0, 1 ),
        ( OrCircuit,   1, 1, 1 ),

        ( AndCircuit,  0, 0 , 0 ),
        ( AndCircuit,  0, 1 , 0 ),
        ( AndCircuit,  1, 0 , 0 ),
        ( AndCircuit,  1, 1, 1 ),

        ( NorCircuit,  1, 1, 0 ),
        ( NorCircuit,  0, 1, 0 ),
        ( NorCircuit,  1, 0, 0 ),
        ( NorCircuit,  0, 0, 1 ),

        ( XorCircuit,  0, 0, 0 ),
        ( XorCircuit, 0, 1, 1 ),
        ( XorCircuit, 1, 0, 1 ),
        ( XorCircuit, 1, 1, 0 ),

        # I added the third value because the loop for testing expects a valQ to test against
        # !The third value is the same as the second!
        ( NotCircuit,  1, 0, 0),
        ( NotCircuit,  0, 1, 1)


    ]
    for circuit, valA, valB, valQ in tests:
        bitA = Bit(valA, name="A")
        bitB = Bit(valB, name="B")
        bitQ = Bit(name="Q")
        c = circuit(bitA, bitB, bitQ)
        c.run()
        if int(bitQ) != valQ:
            print('Error: {}({}, {}): {} != {}'.format(
                circuit.__name__,
                int(bitA), int(bitB), int(bitQ), valQ))
    print('Tests done')
