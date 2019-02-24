#!/usr/bin/env python3

#{{ Remove
# Simulation of Gates and Circuits
# Todo grafical-simulator
# Todo export/import to json
#}} Remove

_version = '0.9'
__author__ = '(c) 2019 Frans Schippers (f.h.schippers@hva.nl) for CSP'
__opgave__ = 'w2_lib'

_map = { '?': None, '0': 0, '1': 1 }
_str = { v: k for k, v in _map.items() }

gVbs = False
def setVerbose(v):
    global gVbs
    gVbs = v
    print('Verbose', gVbs)

class Bit:
    """ Implement a Bit, values None, 0, 1 ('?', '0', '1') """
    def __init__(self, bit=None, name=''):
        """
        Arguments:
            bit  -- Value of the bit
            name -- Name of the bit (optional)
        """
        assert bit in _map.values()

        self.bit = bit
        self.name = name

    def __str__(self):
        """ Verbose info about Bit """
        return '<Bit:{0:2s} bit={1:s}>'.format(self.name, _str.get(self.bit))

    def __int__(self):
        """ Value of Bit """
        if self.bit is None:
            raise ValueError('Uninitialised Bit name={}'.format(self.name))
        return self.bit

    def _peek(self):
        return self.bit

    def get(self):
        """ Get the value of Bit """
        if self.bit is None:
            raise ValueError('Uninitialised Bit name={}'.format(self.name))
        return self.bit

    def set(self, bit):
        """ Set the value of Bit """
        assert bit in _map.values()

#       Set variables can be set again
#       if self.bit is not None:
#           raise ValueError("Initialised Bit: name={}".format(self.name))
        self.bit = bit

class Register:
    """ Implement a Register of n-Bits """
    def __init__(self, n=1, name=''):
        """
        Arguments:
            n      -- Width of the register
            name   -- Name of the register (optional)
        """
        self._name = name
        self._regs = [ Bit() for i in range(n) ]

    @classmethod
    def fromStr(cls, bitStr, name=''):
        """
        Arguments:
            bitStr -- A string with initial value of the bits ('?', '0', '1')
            name   -- Name of the register (optional)
        """
        self = cls(n=len(bitStr), name=name)
        for i, bitChr in enumerate(bitStr):
            bit = _map.get(bitChr, '?')
            name = '{}[{}]'.format(name, i)
            self._regs[i] = Bit(bit=bit, name=name)
        return self

    @classmethod
    def fromInt(cls, i, n, name=''):
        """
        Arguments:
            num    -- The number to store
            n      -- Width of the register
            name   -- Name of the register (optional)
        """
        s = ''.join([ _str.get( 1 if num & 2**i else 0) for i in range(n) ])
        return cls.fromStr(s, name)

    def __str__(self):
        return "<Reg:{} {}>".format(self._name,
                ''.join([ _str.get(r._peek()) for r in self._regs]))

    def __int__(self):
        n = 0
        for i, bit in enumerate(reversed(self._regs)):
            n += bit.get()*2**i
        return n

    def __len__(self):
        return len(self._regs)

    def __getitem__(self, key):
        if not (-len(self._regs) <= key < len(self._regs)):
            raise Exception('Bit: index fault: {}'.format(key))
        return self._regs[key]

    def __setitem__(self, key, bit):
        if not (-len(self._regs) <= key < len(self._regs)):
            raise Exception('Bit: index fault: {}'.format(key))
        if self._regs[key] is not None:
            raise Exception("Set: Initialised reg: {}".format(self._name))
        self._regs[key] = bit

class Gate:
    pass

class Gate_11(Gate):
    def __init__(self, ia, ob):
        """
            Bind the Bits to the gate
            Arguments
                ia: 0 of 1  Input bit
                ob: 0 of 1  Output bit
        """
        self.ia = ia
        self.ob = ob

    def run(self):
        """ Execute the Gate operation. """
        self._run()
        if gVbs:
            print('TRACE: {0:4s} {1:s} set, based on {2:s}'.format(
                    self.oc, self.ia))


class Gate_21(Gate):
    def __init__(self, ia, ib, oc):
        """
            Bind the Bits to the gate
            Arguments
                ia: 0 of 1  Input bit
                ib: 0 of 1  Input bit
                oc: 0 of 1  Output bit
        """
        self.ia = ia
        self.ib = ib
        self.oc = oc

    def run(self):
        """ Execute the Gate operation. """
        self._run()
        if gVbs:
            print('TRACE: {0:4s} {1:s} set, based on {2:s} and {3:s}'.format(
                    self.__class__.__name__, str(self.oc), str(self.ia), str(self.ib)))


class Circuit:
    """ Base-class for Circuits """
    def __init__(self):
        self._circuit = []

    def run(self):
        """ Evaluatie the circuit """
        for gate in self._circuit:
            gate.run()

    def add(self, gate):
        """ Add a gate to the circuit """
        assert isinstance(gate, (Gate, Circuit))

        self._circuit.append(gate)
