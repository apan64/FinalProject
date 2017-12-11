from findPrimeImplicants import findPrimeImplicants
from tabulation import tabulationSingleOutput
from treeFunctions import calcLatency, calcArea

def synthesizeSingleOutput(minTerms, numInputs):
    '''
    Input: list of minTerms
    Output: Head of a tree
    '''
    primeImplicants = findPrimeImplicants(minTerms, numInputs)
    return tabulationSingleOutput(primeImplicants, minTerms)

if __name__ == '__main__':
    test = synthesizeSingleOutput([0, 4, 5, 7, 8, 11, 12, 15], 4)
    print(calcLatency(test))
    print(calcArea(test))
    print(test.eval({'a': True, 'b': True, 'c': True, 'd':True})) # 1111 t
    print(test.eval({'a': False, 'b': False, 'c': False, 'd':False})) # 0000 t
    print(test.eval({'a': False, 'b': True, 'c': False, 'd':False})) # 0100 t
    print(test.eval({'a': False, 'b': True, 'c': True, 'd':False})) # 0110 f