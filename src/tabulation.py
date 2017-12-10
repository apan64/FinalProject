def cost(PI):
	return 1 + sum(1 for x in PI if x != '-')

def findCombinations(pisList):
    if (len(pisList) == 0):
        return [set()]
    recurCall = findCombinations(pisList[1:])
    ans = []
    for pi in pisList[0]:
        for s in recurCall:
            ans.append(set([pi]).union(s))
    return ans

def convertToTree(comb):
    '''
    Input: list of tuples, where each tuple represents a prime implicant
    Output: head node of tree
    '''
    numInputs = len(comb[0])
    inputs = set()
    for pi in comb:
        for i, val in enumerate(pi):
            if (val != '-'):
                inputs.add(chr(97 + i))
    print(inputs)
    return


def tabulationSingleOutput(primeImplicants, minTerms):
    '''
    Input: dictionary mapping prime implicants to the minTerms they cover
    Output: head node of tree
    '''
    piAns = set()
    dominated = set()

    # populating mapping from each minTerm to the prime implicants that cover it
    # identify dominated rows
    minTermsToPI = {mt: [] for mt in minTerms}
    for pi, mts in primeImplicants.items():
        shared = set(minTermsToPI[mts[0]])
        for i, mt in enumerate(mts):
            minTermsToPI[mt].append(pi)
            shared = set(p for p in minTermsToPI[mt] if p in shared)
        if (len(shared) > 0):
            dominated.add(pi)

    # find essential prime implicants (ones that need to include in solution)
    for mt, pis in minTermsToPI.items():
        if (len(pis) == 1):
            piAns.add(pis[0])

    # remove essentials from the mapping
    for pi in piAns:
        for mt in primeImplicants[pi]:
            if mt in minTermsToPI:
                del minTermsToPI[mt]

    # produce combinations that cover all minterms, then choose lowest cost one
    pisList = [pis for mt, pis in minTermsToPI.items()]
    possibleComb = findCombinations(pisList)
    bestComb = list(piAns.union(min(possibleComb, key = lambda comb: sum(cost(c) for c in comb))))
    print(bestComb)
    return convertToTree(bestComb)

print(tabulationSingleOutput({('1', '1', '-', '0'): [1, 4], ('1', '-', '-', '0'): [2, 4, 7], ('-', '0', '1', '1'): [5], ('0', '1', '-', '-'): [1, 4, 5]}, [1, 2, 4, 5, 7]))

    
