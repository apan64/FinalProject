from collections import defaultdict, namedtuple
from itertools import chain

Implicant = namedtuple('Implicant', ['bin_str', 'minterms', 'isPrime', 'fnTags'])


def findPrimeImplicants(fnToMinTerms, num_inputs):
    """Finds the prime implicants of a logical net using the Quine-McCluskey algorithm.
    Input:
        fnToMinTerms: [[int]]. binary values of the parameters when the logical net equals 1.
        num_inputs: int, # of inputs to our logical net
    Output: [{pi: minterms}] where pi is a string like "010-"
     """
    # Step 0: Format input
    all_terms = list(set(chain.from_iterable(fnToMinTerms)))
    # 2 -> '010', 3 -> '011'
    bin_rep = ["{0:b}".format(t).zfill(num_inputs) for t in all_terms]
    # Store which minTerm belongs to which function
    tags = {}
    for t in all_terms:
        tag = ""
        for minTerms in fnToMinTerms:
            tag += "1" if t in minTerms else "0"
        tags[t] = tag

    current_implicants = [Implicant(b, frozenset([t]), True, tags[t]) for (b, t) in zip(bin_rep, all_terms)]

    prime_implicants = []
    for i in range(num_inputs):
        # Step 1: Group minterms based on # of 1's
        grouped = groupByNum1s(current_implicants)
        # Step 2: Apply adjacency property to reduce implicants
        new_implicants = []
        for i in range(num_inputs):
            n, grouped[i], grouped[i+1] = reduce(grouped[i], grouped[i+1])
            new_implicants += n
        vals = sum(list(grouped.values()), [])
        prime_implicants += list(filter(lambda x: x.isPrime, vals))
        current_implicants = new_implicants
    return prime_implicants


def groupByNum1s(implicants):
    """Groups a list of binary strings into lists based on the # of 1s"""
    grouped = defaultdict(list)
    for i in implicants:
        num_1s = sum([bit is '1' for bit in i.bin_str])
        grouped[num_1s].append(i)
    return grouped


def reduce(implicants_1, implicants_2):
    """ takes 2 lists of implicants and
        returns a list of the reduced implicants
        and implicants marked prime/not prime
    ."""
    if len(implicants_1) == 0 or len(implicants_2) == 0:
        return([], implicants_1, implicants_2)
    ret = set()
    for j, i_1 in enumerate(implicants_1):
        for k, i_2 in enumerate(implicants_2):
            diff_letters = sum(x != y for x, y in zip(i_1.bin_str, i_2.bin_str))
            if diff_letters == 1:
                if hasCommonLetter(i_1.fnTags, i_2.fnTags, "1"):
                    combined = ''.join(['-' if x != y else x for x, y in zip(i_1.bin_str, i_2.bin_str)])
                    newTag = combineTags(i_1.fnTags, i_2.fnTags)
                    ret.add(Implicant(combined, i_1.minterms | i_2.minterms, True, newTag))
                    # Only set implicants to false if the new tag is
                    # The same as the old ones
                    if newTag == i_1.fnTags == i_2.fnTags:
                        # Set the used implicants as not prime
                        implicants_1[j] = Implicant(i_1.bin_str, i_1.minterms, False, i_1.fnTags)
                        implicants_2[k] = Implicant(i_2.bin_str, i_2.minterms, False, i_2.fnTags)
    return list(ret), implicants_1, implicants_2


def hasCommonLetter(a, b, l):
    """ Returns true if both string contain a letter at the same position"""
    for (x, y) in zip(a, b):
        if x == y == l:
            return True
    return False


def combineTags(tag1, tag2):
    """ Combines two function tags."""
    ret = ""
    for (x, y) in zip(tag1, tag2):
        ret += "1" if int(x) & int(y) else "0"
    return ret

asdf = findPrimeImplicants([[2, 3, 7], [4, 5, 7]], 3)
for p in asdf:
    print(p)
# a, b, c = reduce([
#               Implicant(bin_str='010', minterms=frozenset({2}), isPrime=True, fnTags='10'),
#               Implicant(bin_str='100', minterms=frozenset({4}), isPrime=True, fnTags='01')
#               ],
#               [
#               Implicant(bin_str='011', minterms=frozenset({3}), isPrime=True, fnTags='10'),
#               Implicant(bin_str='101', minterms=frozenset({5}), isPrime=True, fnTags='01')
#               ])
# print(a)
