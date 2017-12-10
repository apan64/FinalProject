def synthesizeSingleOutput(minTerms):
	'''
	Input: list of minTerms
	Output: Head of a tree
	'''
	primeImplicants = findPrimeImplicantsSingleOutput(minTerms)
	return tabulationSingleOutput(primeImplicants, minTerms)