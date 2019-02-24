#!/usr/bin/env python3

_version = '1.0'
__author__ = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP'
__opgave__ = 'w2o1'

from w2_lib import *

# Extensions for gates:
class Not(Gate_11):
    """ Implementation of Not-gate """
    def _run(self):
        self.ob.set( self.ia.get() ^ 1 )

class Nand(Gate_21):
    """ Implementation of Nand-gate """
    def _run(self):
        self.oc.set( ( ( self.ia.get() & self.ib.get() ) ^ 1 ) )

class And(Gate_21):
    """ Implementation of And-gate """
    def _run(self):
        output = Bit()
        nand = Nand(self.ia, self.ib, output)
        nand.run()
        nandOutput = output

        nand = Nand(nandOutput, nandOutput, output)
        nand.run()

        self.oc.set(output.get())

class Or(Gate_21):
    """ Implementation of Or-gate """
    def _run(self):
        output = Bit()

        nand = Nand(self.ia, self.ia, output)
        nand.run()
        firstNandResult = output

        output = Bit();

        nand = Nand(self.ib, self.ib, output)
        nand.run()
        secondNandResult = output

        nand = Nand(firstNandResult, secondNandResult, output)
        nand.run()

        self.oc.set(output.get())

class Nor(Gate_21):
    """ Implementation of Nor-gate """
    def _run(self):
        output = Bit()

        nand = Nand(self.ia, self.ia, output)
        nand.run()
        firstNandResult = output

        output = Bit();

        nand = Nand(self.ib, self.ib, output)
        nand.run()
        secondNandResult = output

        nand = Nand(firstNandResult, secondNandResult, output)
        nand.run()


        nand = Nand(output, output, output)
        nand.run()

        self.oc.set(output.get())

class Xor(Gate_21):
    """ Implementation of Xor-gate """
    def _run(self):
        output = Bit()

        nand = Nand(self.ia, self.ib, output)
        nand.run()
        firstOutput = output

        output = Bit()

        nand = Nand(self.ia, firstOutput, output)
        nand.run()
        lastOutputA = output;

        output = Bit()

        nand = Nand(self.ib, firstOutput, output)
        nand.run()
        lastOutputB = output

        output = Bit()

        nand = Nand(lastOutputA, lastOutputB, output)
        nand.run()

        self.oc.set(output.get())


if __name__ == '__main__':
    # Tests for sub-classes of Gate_11
    tests =  [
        ( Not, 0, 1 ),
        ( Not, 1, 0 ),
    ]
    for gate, iValA, oValB in tests:
        iBitA = Bit(iValA)
        oBitB = Bit()
        g = gate(iBitA, oBitB)
        g.run()
        if oBitB.get() != oValB:
            print('Error: {}({}): {} != {}'.format(
                g.__name__, iValA, oBitB, oValB))

    # Tests for sub-classes of Gate_21
    tests =  [
        ( Nand, 0, 0, 1 ),
        ( Nand, 0, 1, 1 ),
        ( Nand, 1, 0, 1 ),
        ( Nand, 1, 1, 0 ),

        ( Nor,  0, 0, 1 ),
        ( Nor,  0, 1, 0 ),
        ( Nor,  1, 0, 0 ),
        ( Nor,  1, 1, 0 ),

        ( And,  0, 0, 0 ),
        ( And,  0, 1, 0 ),
        ( And,  1, 0, 0 ),
        ( And,  1, 1, 1 ),

        ( Or,   0, 0, 0 ),
        ( Or,   0, 1, 1 ),
        ( Or,   1, 0, 1 ),
        ( Or,   1, 1, 1 ),

        ( Xor,  0, 0, 0 ),
        ( Xor,  0, 1, 1 ),
        ( Xor,  1, 0, 1 ),
        ( Xor,  1, 1, 0 ),
    ]
    for gate, iValA, iValB, oValC in tests:
        iBitA = Bit(iValA)
        iBitB = Bit(iValB)
        oBitC = Bit()
        g = gate(iBitA, iBitB, oBitC)
        g.run()
        if oBitC.get() != oValC:
            print('Error: {}({}, {}): {} != {}'.format(
                g.__class__.__name__, iBitA, iBitB, oBitC, oValC))

    print('Tests done')
