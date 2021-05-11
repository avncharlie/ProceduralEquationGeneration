from sympy import *
import shutil
import random


def clear():
    """
    Clears the screen
    """
    print("\033c", end="")

init_printing(use_unicode=True)

randomRange = [Integer(x) for x in range(1, 100)]

ops = [
        (lambda x: Add(random.choice(randomRange), x), lambda x: x),
        (lambda x: Mul(random.choice(randomRange), x), lambda x: x),
        (lambda x: Mul(random.choice(randomRange), Pow(x, Integer(-1))), lambda x: x),
        (lambda x: Mul(x, Integer(1)/(random.choice(randomRange))), lambda x: x),
        (log, exp),
        (lambda x: Pow(x, Rational(1, 2)), sqrt),
        (sin, asin),
]

RHS = Integer(random.choice(range(1, 10)))
LHS = symbols('x')

backtrack = []

while True:
    screenSpace = shutil.get_terminal_size().lines

    generated = Eq(LHS, RHS)

    clear()
    
    print("\n"*int(screenSpace/3+1))

    pprint(generated)

    input()

    op = random.choice(ops)
    choice = random.choice([0,1]) * 0  # force 0 while working 
    chosenOpp = op[choice]
    backtrack.append(op[choice^1])

    LHS = chosenOpp(LHS)
    RHS = chosenOpp(RHS)

    RHS = simplify(RHS)
