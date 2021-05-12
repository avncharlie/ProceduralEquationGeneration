"""
    - probabilities of used functions

    - combination of atoms
        - atom similarity hueristic

    - sympy simplification

    - filtering

    - generation solution

    - filtering

expr = a

solve

answer: x = f(a)


sin(x)+1 = a

answer: asin(a-1)

asin(45) = 1/sqrt(2)

a - 1 = 45

a = 46

2a/5
a = 5/2

"""

inIPython = False
try:
    from IPython.display import display
    inIPython = True
except:
    pass

import random
from sympy import *
import Operations

class mathGenerator:

    fillerNumRange = (1, 20)
    nestingRange = (1, 5)

    def __init__(self, symbol=symbols('x')):
        self.symbol = symbol
        self.expr = symbol 

        # types are simple, trigonometry, exponential, power
        self.opps = Operations.allOperations
    def gen(self):
        a = self.createAtom(self.symbol)
        pprint(a)

    def createAtom(self, symbol=symbols('x')):
        # start with just the symbol
        atom = symbol

        # random level of nesting
        nest = random.randint(*mathGenerator.nestingRange)
        alreadyApplied = ['_']

        # returns list of complex function types applied
        complexFuncTypeAlreadyApplied = lambda t: t in \
                [info['type'] for _, info in alreadyApplied[1:] \
                if info['type'] != 'simple']

        for x in range(nest):
            # choose next function to apply
            funcName, funcInfo = self.chooseRandomOpp()

            # don't apply same function twice in a row
            # don't apply more than one of each trig, exponential or power function
            while alreadyApplied[-1][0] == funcName or complexFuncTypeAlreadyApplied(funcInfo['type']):
                funcName, funcInfo = self.chooseRandomOpp()

            alreadyApplied.append((funcName, funcInfo))

            # if double input function, generate the second input
            if funcInfo['numInputs'] == 2:
                # generate random number for second input
                secondVal = random.choice(range(*mathGenerator.fillerNumRange))
                
                # if double input function has a generator, use that instead
                if 'secondInputGen' in funcInfo.keys():
                    secondVal = (funcInfo['secondInputGen'])()

                atom = (funcInfo['func'])(atom, secondVal)

            # if single input expression, pass atom into it
            elif funcInfo['numInputs'] == 1:
                atom = (funcInfo['func'])(atom)

        return atom

    # use with operationsOfType to choose random operation of type
    # return (name, info)
    def chooseRandomOpp(self, opps=Operations.allOperations):
        return random.choice(list(opps.items()))

if __name__ == "__main__":
    init_printing(use_unicode=True)
            
    x,a = symbols('x a')

    generator = mathGenerator(x)
    atom = generator.createAtom()

    #expression = Eq(atom, random.randint(1, 10))
    #expression = Eq(atom, a)
    expression = atom
    out = [expression]
    #out.append(solve(expression, x))
    
    if inIPython:
        for x in out: display(x)
    else:
        for x in out: pprint(x)
