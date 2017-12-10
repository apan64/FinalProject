def synthesizeSingleOutput(minTerms):
	'''
	Input: list of minTerms
	Output: Head of a tree
	'''
	primeImplicants = findPrimeImplicants(minTerms)
	return tabulationSingleOutput(primeImplicants, minTerms)
