from gatesim import *

if __name__ == '__main__':
    c = Circuit()
    regA = Register.fromStr(bitStr="1100", name="A")
    regB = Register.fromStr(bitStr="1101", name="B")
    regC = Register(n=4, name="C")
    c.add(Adder(regA, regB, regC, n=4))
    c.run()
    print('{} + {} = {}'.format(
        int(regA), int(regB), int(regC)))
