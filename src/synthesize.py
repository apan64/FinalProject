from findPrimeImplicants import findPrimeImplicants
from tabulation import tabulationSingleOutput, tabulationMultipleOutput
from treeFunctions import calcLatency, calcArea

def synthesizeSingleOutput(minTerms, numInputs):
    '''
    Input: list of minTerms
    Output: Head of a tree
    '''
    primeImplicants = findPrimeImplicants(minTerms, numInputs)
    return tabulationSingleOutput(primeImplicants, minTerms)

def synthesizeMultipleOutput(minTerms, numInputs):
    primeImplicants = findPrimeImplicants(minTerms, numInputs)
    return tabulationMultipleOutput(primeImplicants, minTerms)

if __name__ == '__main__':
    print('Test 1')
    test = synthesizeSingleOutput([[0, 4, 5, 7, 8, 11, 12, 15]], 4)
    print(calcLatency(test))
    print(calcArea(test))
    print(test.eval({'a': True, 'b': True, 'c': True, 'd':True})) # 1111 t
    print(test.eval({'a': False, 'b': False, 'c': False, 'd':False})) # 0000 t
    print(test.eval({'a': False, 'b': True, 'c': False, 'd':False})) # 0100 t
    print(test.eval({'a': False, 'b': True, 'c': True, 'd':False})) # 0110 f

    print('Test 2')
    test2 = synthesizeMultipleOutput([[2, 3, 7], [4, 5, 7]], 3)
    for logic in test2:
        print(logic.eval({'a': True, 'b': True, 'c': True})) #111 t t
        print(logic.eval({'a': False, 'b': True, 'c': True})) #011 t f
        print(logic.eval({'a': True, 'b': False, 'c': True})) #101 f t
        print(logic.eval({'a': False, 'b': False, 'c': False})) #000 f f

    print('Test adder')
    adder = synthesizeMultipleOutput([[1, 2, 4, 7], [3, 5, 6, 7]], 3)
    for i, logic in enumerate(adder):
        if (i == 0):
            print('Sum')
        else:
            print('Cout')
        print(calcLatency(logic))
        print(calcArea(logic))
        print(logic.eval({'a': True, 'b': True, 'c': True})) #111 t t
        print(logic.eval({'a': True, 'b': True, 'c': False})) #110 f t
        print(logic.eval({'a': True, 'b': False, 'c': True})) #101 f t
        print(logic.eval({'a': True, 'b': False, 'c': False})) #100 t f
        print(logic.eval({'a': False, 'b': True, 'c': True})) #011 f t
        print(logic.eval({'a': False, 'b': True, 'c': False})) #010 t f
        print(logic.eval({'a': False, 'b': False, 'c': True})) #001 t f
        print(logic.eval({'a': False, 'b': False, 'c': False})) #000 f f