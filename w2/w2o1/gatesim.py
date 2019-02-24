#!/usr//bin/env python3

__author__ = '(c) 2018 HvA.nl, f.h.schippers@hva.nl'

import gatesimlib as gs
from gatesimlib import *

class NandCircuit(Circuit):
    """ Implement a And circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitC):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitC   -- Output C (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitC, Bit)

        Circuit.__init__(self)
        self.add(Nand(iBitA, iBitA, oBitC))

class OrCircuit(Circuit):
    """ Implement a Or circuit using Nand-gates """
    def __init__(self, iBitA, iBitB, oBitC):
        """
        Arguments:
            iBitA   -- Input  A (Bit, initialized)
            iBitB   -- Input  B (Bit, initialized)
            oBitC   -- Output C (Bit, not initialized)
        """
        assert isinstance(iBitA, Bit) and isinstance(iBitB, Bit)
        assert isinstance(oBitC, Bit)

        Circuit.__init__(self)
        tBit1 = Bit(name='t1')
        tBit2 = Bit(name='t2')
        self.add(Nand(iBitA, iBitA, tBit1))
        self.add(Nand(iBitB, iBitB, tBit2))
        self.add(Nand(tBit1, tBit2, oBitC))

if __name__ == '__main__':
    setVerbose(True)

    bitA = Bit(0, name="A")
    bitB = Bit(1, name="B")
    bitC = Bit(name="C")
    c = NandCircuit(bitA, bitB, bitC)
    c.run()
    print('{} NAND {} = {}'.format(
        int(bitA), int(bitB), int(bitC)))
    print('{} NAND {} = {}'.format(
        str(bitA), str(bitB), str(bitC)))

    bitA = Bit(0, name="A")
    bitB = Bit(1, name="B")
    bitC = Bit(name="C")
    c = OrCircuit(bitA, bitB, bitC)
    c.run()
    print('{} OR {} = {}'.format(
        int(bitA), int(bitB), int(bitC)))
    print('{} OR {} = {}'.format(
        str(bitA), str(bitB), str(bitC)))
