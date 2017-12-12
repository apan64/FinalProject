from findPrimeImplicants import findPrimeImplicants
from tabulation import tabulationSingleOutput, tabulationMultipleOutput
from treeFunctions import calcLatency, calcArea, calcAreaMultiHead
from generate_alu_4bit import genALU4bitMT

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

    print('\n\nTest alu')
    alu = synthesizeMultipleOutput([[8, 16, 9, 17, 10, 18, 11, 28, 5, 13, 21, 29, 6, 15, 23, 31], [24], [9]], 5)
    expected = [(0, 1, 0, 1, 1), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)]
    tests = [{'a': False, 'b': False, 'c': False, 'd': False, 'e': False}, {'a': False, 'b': True, 'c': False, 'd': False, 'e': False}, {'a': True, 'b': True, 'c': False, 'd': False, 'e': False}, {'a': False, 'b': True, 'c': False, 'd': False, 'e': True}, {'a': True, 'b': True, 'c': True, 'd': True, 'e': True}]
    print('Area: {}'.format(calcAreaMultiHead(alu)))
    for i, logic in enumerate(alu):
        print('Part {} Latency: {}'.format(i + 1, calcLatency(logic)))
        for j, t in enumerate(tests):
            if (logic.eval(t) != expected[i][j]):
                print('Part {} Test {} failed'.format(i + 1, j + 1))
    print(alu)

    # print('\n\nTest 4 bit alu')
    # alu4bit = synthesizeMultipleOutput(genALU4bitMT(), 11)
    # print(alu4bit)
    # expected = [(0, 1, 0, 1, 1), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0)]
    # tests = [{'a': False, 'b': False, 'c': False, 'd': False, 'e': False}, {'a': False, 'b': True, 'c': False, 'd': False, 'e': False}, {'a': True, 'b': True, 'c': False, 'd': False, 'e': False}, {'a': False, 'b': True, 'c': False, 'd': False, 'e': True}, {'a': True, 'b': True, 'c': True, 'd': True, 'e': True}]
    # print('Area: {}'.format(calcAreaMultiHead(alu4bit)))
    # for i, logic in enumerate(alu4bit):
    #     print('Part {} Latency: {}'.format(i + 1, calcLatency(logic)))
    #     for j, t in enumerate(tests):
    #         if (logic.eval(t) != expected[i][j]):
    #             print('Part {} Test {} failed'.format(i + 1, j + 1))