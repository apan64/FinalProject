from findPrimeImplicants import findPrimeImplicants
from tabulation import tabulationSingleOutput

def synthesizeSingleOutput(minTerms, numInputs):
    '''
    Input: list of minTerms
    Output: Head of a tree
    '''
    primeImplicants = findPrimeImplicants(minTerms, numInputs)
    return tabulationSingleOutput(primeImplicants, minTerms)

synthesizeSingleOutput([0, 4, 5, 7, 8, 11, 12, 15], 4)