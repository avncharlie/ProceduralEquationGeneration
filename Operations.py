from sympy import *

# combiner = can combine atoms
# if used in generation, use random constant as second atom
# multiple input non combiner functions have generations in the 'secondInputGen'
# to use as the second input

# types are simple, trigonometry, exponential, power
allOperations = {
        'add': {
            'func': Add,
            'atomCombiner': True,
            'numInputs': 2,
            'type': 'simple'
        },

        'subtract': {
            'func': lambda x, y: Add(x, Mul(Integer(-1), y)),
            'atomCombiner': True,
            'numInputs': 2,
            'type': 'simple'
        },

        'multiply': {
            'func': Mul,
            'atomCombiner': True,
            'numInputs': 2,
            'type': 'simple'
        },

        'divide': {
            'func': lambda x, y: Mul(x, Pow(y, Integer(-1))),
            'atomCombiner': True,
            'numInputs': 2,
            'type': 'simple'
        },

        'power': {
            'func': Pow,
            'atomCombiner': False,
            'numInputs': 2,
            'secondInputGen': lambda: 2,
            'type': 'power'
        },

        'root': {
            'func': lambda x, y: Pow(x, Rational(1, y)),
            'atomCombiner': False,
            'numInputs': 2,
            'secondInputGen': lambda: 2,
            'type': 'power'
        },

        'logarithm': {
            'func': log,
            'atomCombiner': False,
            'numInputs': 1,
            'type': 'exponentials'
        },

        'exponential': {
            'func': exp,
            'atomCombiner': False,
            'numInputs': 1,
            'type': 'exponentials'
        },

        'sine': {
            'func': sin,
            'atomCombiner': False,
            'numInputs': 1,
            'type': 'trigonometry'
        },

        'cosine': {
            'func': cos,
            'atomCombiner': False,
            'numInputs': 1,
            'type': 'trigonometry'
        },

        'tangent': {
            'func': tan,
            'atomCombiner': False,
            'numInputs': 1,
            'type': 'trigonometry'
        }
}

def operationsOfType(t):
    return {name:info for name, info in allOperations.items() if info['type'] == t}
