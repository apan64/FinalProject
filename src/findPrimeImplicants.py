from collections import defaultdict


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
    implicants.append(list(zip(bin_rep, minterms)))
    grouped = groupByNum1s(implicants[0])
    print(reduce(grouped[2], grouped[3]))

    # Step 2: Apply adjacency property to reduce implicants


def groupByNum1s(implicants):
    """Groups a list of binary strings into lists based on the # of 1s"""
    grouped = defaultdict(list)
    for i in implicants:
        bin_str = i[0]
        print(i)
        num_1s = sum([int(bit) for bit in bin_str])
        grouped[num_1s].append(i)
    return grouped


def reduce(implicants_1, implicants_2):
    """ takes 2 lists of implicants and
        returns a list of the reduced implicants
    ."""
    if implicants_1 is [] or implicants_2 is []:
        return []
    ret = []
    for i_1 in implicants_1:
        for i_2 in implicants_2:
            bin_1, min_t_1 = i_1
            bin_2, min_t_2 = i_2
            diff_letters = sum(x != y for x, y in zip(bin_1, bin_2))
            if diff_letters == 1:
                combined = ''.join(['-' if x != y else x for x, y in zip(bin_1, bin_2)])
                ret.append((combined, [min_t_1, min_t_2]))
    return ret


findPrimeImplicants([2, 3, 7, 5], 3)
