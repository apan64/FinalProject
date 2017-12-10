from collections import defaultdict, namedtuple

Implicant = namedtuple('Implicant', ['bin_str', 'minterms', 'isPrime'])


def findPrimeImplicants(minterms, num_inputs):
    """Finds the prime implicants of a logical net using the Quine-McCluskey algorithm.
    Input:
        minterms: [int]. binary values of the parameters when the logical net equals 1.
        num_inputs: int, # of inputs to our logical net
    Output: [{pi: minterms}] where pi is a string like "010-"
     """
    # Step 1: Group minterms based on # of 1's
    # implicants[0] is implicants with 0 overlaps
    # implicants[n] is implicants with n overlaps
    implicants = []
    # 2 -> '010', 3 -> '011'
    bin_rep = ["{0:b}".format(t).zfill(num_inputs) for t in minterms]
    implicants.append(Implicant(b, [m], True) for (b, m) in zip(bin_rep, minterms))
    grouped = groupByNum1s(implicants[0])

    # Step 2: Apply adjacency property to reduce implicants
    new_implicants = []
    for i in range(num_inputs):
        n, grouped[i], grouped[i+1] = reduce(grouped[i], grouped[i+1])
        new_implicants += n


def groupByNum1s(implicants):
    """Groups a list of binary strings into lists based on the # of 1s"""
    grouped = defaultdict(list)
    for i in implicants:
        print(i)
        num_1s = sum([int(bit) for bit in i.bin_str])
        grouped[num_1s].append(i)
    return grouped


def reduce(implicants_1, implicants_2):
    """ takes 2 lists of implicants and
        returns a list of the reduced implicants
        and implicants marked prime/not prime
    ."""
    if implicants_1 is [] or implicants_2 is []:
        return [], implicants_1, implicants_2
    ret = []
    for j, i_1 in enumerate(implicants_1):
        for k, i_2 in enumerate(implicants_2):
            diff_letters = sum(x != y for x, y in zip(i_1.bin_str, i_2.bin_str))
            if diff_letters == 1:
                combined = ''.join(['-' if x != y else x for x, y in zip(i_1.bin_str, i_2.bin_str)])
                ret.append(Implicant(combined, i_1.minterms+i_2.minterms, True))
                # Set the used implicants as not prime
                implicants_1[j] = Implicant(i_1.bin_str, i_1.minterms, False)
                implicants_2[k] = Implicant(i_2.bin_str, i_2.minterms, False)
    return ret, implicants_1, implicants_2


findPrimeImplicants([2, 3, 7, 5], 3)
