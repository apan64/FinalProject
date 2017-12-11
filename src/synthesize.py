from findPrimeImplicants import findPrimeImplicants
from tabulation import tabulationSingleOutput, tabulationMultipleOutput
from treeFunctions import calcLatency, calcArea, calcAreaMultiHead

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
    expected = [True, True, True, False]
    print('Latency: {}'.format(calcLatency(test)))
    print('Area: {}'.format(calcArea(test)))
    answers = [test.eval({'a': True, 'b': True, 'c': True, 'd':True}), test.eval({'a': False, 'b': False, 'c': False, 'd':False}), test.eval({'a': False, 'b': True, 'c': False, 'd':False}), test.eval({'a': False, 'b': True, 'c': True, 'd':False})]
    for i, ans in enumerate(answers):
        if (ans != expected[i]):
            print('Test {} failed'.format(i + 1))

    print('\n\nTest 2')
    test2 = synthesizeMultipleOutput([[2, 3, 7], [4, 5, 7]], 3)
    expected = [(True, True, False, False), (True, False, True, False)]
    print('Area: {}'.format(calcAreaMultiHead(test2)))
    tests = ({'a': True, 'b': True, 'c': True}, {'a': False, 'b': True, 'c': True}, {'a': True, 'b': False, 'c': True}, {'a': False, 'b': False, 'c': False})
    for i, logic in enumerate(test2):
        print('Part {} Latency: {}'.format(i + 1, calcLatency(logic)))
        for j, t in enumerate(tests):
            if (logic.eval(t) != expected[i][j]):
                print('Part {} Test {} failed'.format(i + 1, j + 1))

    print('\n\nTest adder')
    adder = synthesizeMultipleOutput([[1, 2, 4, 7], [3, 5, 6, 7]], 3)
    expected = [(True, False, False, True, False, True, True, False), (True, True, True, False, True, False, False, False)]
    tests = [{'a': True, 'b': True, 'c': True}, {'a': True, 'b': True, 'c': False}, {'a': True, 'b': False, 'c': True}, {'a': True, 'b': False, 'c': False}, {'a': False, 'b': True, 'c': True}, {'a': False, 'b': True, 'c': False}, {'a': False, 'b': False, 'c': True}, {'a': False, 'b': False, 'c': False}]
    print('Area: {}'.format(calcAreaMultiHead(adder)))
    for i, logic in enumerate(adder):
        print('Part {} Latency: {}'.format(i + 1, calcLatency(logic)))
        for j, t in enumerate(tests):
            if (logic.eval(t) != expected[i][j]):
                print('Part {} Test {} failed'.format(i + 1, j + 1))
