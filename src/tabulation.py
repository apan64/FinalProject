from eqNodes import VariableNode, UnaryNode, BinaryNode
from collections import deque

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

def computeCombinations(implicants, minTerms):
    primeImplicants = {i.bin_str: list(i.minterms) for i in implicants}
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
    return (findCombinations(pisList), piAns)


def convertToTree(combs):
    '''
    Input: list of tuples, where each tuple represents a prime implicant
    Output: head node of tree
    '''
    numInputs = len(combs[0])
    inputs = set()
    for comb in combs:
        for i, val in enumerate(comb):
            if (val != '-'):
                inputs.add(chr(97 + i))
    inputNodes = {i: VariableNode(i) for i in inputs}
    orQ = deque()
    for comb in combs:
        q = deque()
        for i, val in enumerate(comb):
            if (val == '1'):
                q.append(inputNodes[chr(97 + i)])
            elif (val == '0'):
                q.append(UnaryNode(fn = lambda x: not(x), name = 'not', arg1 = inputNodes[chr(97 + i)]))
        while len(q) > 1:
            q.append(BinaryNode(fn = lambda x, y: (x and y), name = 'and', arg1 = q.popleft(), arg2 = q.popleft()))
        orQ.append(q.popleft())
    while len(orQ) > 1:
        orQ.append(BinaryNode(fn = lambda x, y: (x or y), name = 'or', arg1 = orQ.popleft(), arg2 = orQ.popleft()))
    return orQ.popleft()

def convertToTreeMultiple(combs):
    '''
    Input: list of list of tuples, where each tuple represents a prime implicant
    Output: list of head nodes of trees
    '''
    numInputs = len(combs[0])
    inputs = set()
    for comb in combs:
        for pis in comb:
            for i, val in enumerate(pis):
                if (val != '-'):
                    inputs.add(chr(97 + i))
    inputNodes = {i: VariableNode(i) for i in inputs}
    ans = []
    done = {}
    for comb in combs:
        orQ = deque()
        for pis in comb:
            q = deque()
            for i, val in enumerate(pis):
                if (val == '1'):
                    q.append(inputNodes[chr(97 + i)])
                elif (val == '0'):
                    un = UnaryNode(fn = lambda x: not(x), name = 'not', arg1 = inputNodes[chr(97 + i)])
                    unStr = un.toString()
                    if unStr not in done:
                        done[unStr] = un
                        q.append(un)
                    else:
                        q.append(done[unStr])
            while len(q) > 1:
                binary = BinaryNode(fn = lambda x, y: (x and y), name = 'and', arg1 = q.popleft(), arg2 = q.popleft())
                binStr = binary.toString()
                if binStr not in done:
                    done[binStr] = binary
                    q.append(binary)
                else:
                    q.append(done[binStr])
            orQ.append(q.popleft())
        while len(orQ) > 1:
            binary = BinaryNode(fn = lambda x, y: (x or y), name = 'or', arg1 = orQ.popleft(), arg2 = orQ.popleft())
            binStr = binary.toString()
            if binStr not in done:
                done[binStr] = binary
                orQ.append(binary)
            else:
                orQ.append(done[binStr])
        ans.append(orQ.popleft())
    return ans


def tabulationSingleOutput(implicants, minTerms):
    '''
    Input: dictionary mapping prime implicants to the minTerms they cover
    Output: head node of tree
    '''
    possibleComb, piAns = computeCombinations(implicants, minTerms[0])
    bestComb = list(piAns.union(min(possibleComb, key = lambda comb: sum(cost(c) for c in comb))))
    return convertToTree(bestComb)

def tabulationMultipleOutput(implicants, minTermsInputs):
    outputImplicants = [[] for i in range(len(minTermsInputs))]
    for imp in implicants:
        for i, char in enumerate(imp.fnTags):
            if (char == '1'):
                outputImplicants[i].append(imp)
    outputCombinations = [computeCombinations(imp, minTermsInputs[i]) for i, imp in enumerate(outputImplicants)]
    bestCombinations = [list(piAns.union(min(possibleComb, key = lambda comb: sum(cost(c) for c in comb)))) for possibleComb, piAns in outputCombinations]
    bestCost = [(sum(cost(c) for c in comb)) for comb in bestCombinations]
    for i, combinationTup in enumerate(outputCombinations):
        for comb in combinationTup[0]:
            for term in comb:
                curCost = sum(cost(c) for c in comb) + sum(cost(c) for c in combinationTup[1]) + sum(bestCost[:i])
                curComb = ['' for _ in range(len(outputCombinations))]
                curComb[i] = comb
                for j, combinationTup2 in enumerate(outputCombinations[i + 1:]):
                    curCost += sum(cost(c) for c in combinationTup2[1])
                    notAdded = True
                    for comb2 in combinationTup2[0]:
                        if (term in comb2):
                            curCost += sum(cost(c) for c in comb2) - cost(term)
                            curComb[i + j + 1] = comb2
                            notAdded = False
                    if (notAdded):
                        curCost += bestCost[i + j + 1]
                if (curCost < sum(bestCost)):
                    for replacementI, replacementComb in enumerate(curComb):
                        if replacementComb != '':
                            bestCombinations[replacementI] = replacementComb.union(set(outputCombinations[replacementI][1]))
                            bestCost[replacementI] = sum(cost(c) for c in replacementComb)
    return convertToTreeMultiple(bestCombinations)
