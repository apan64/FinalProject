from itertools import product

def multiplyBits(inputs, bits):
    return sum(inputs[i] * bit for i, bit in enumerate(bits))

def genALU4bitMT():
    a1 = 1
    a2 = 2
    a3 = 4
    a4 = 8
    b1 = 16
    b2 = 32
    b3 = 64
    b4 = 128
    fn1 = 256
    fn2 = 512
    fn3 = 1024
    inputs = [a1, a2, a3, a4, b1, b2, b3, b4, fn1, fn2, fn3]
    inputsToPorts = {inp: i for i, inp in enumerate(inputs)}
    bits = product((0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1))
    outputs = [[], [], [], [], [], [], []]
    for bit in bits:
        curNum = multiplyBits(inputs, bit)
        carry0 = 0
        # addition
        if (bit[8] == 0 and bit[9] == 0 and bit[10] == 0):
            zero = True
            # bit 1
            carry1 = 0
            if (bit[inputsToPorts[a1]] ^ bit[inputsToPorts[b1]] == 1):
                outputs[0].append(curNum)
                zero = False
            elif (bit[inputsToPorts[a1]] + bit[inputsToPorts[b1]] == 2):
                carry1 = 1
            # bit 2
            if (bit[inputsToPorts[a2]] + bit[inputsToPorts[b2]] + carry1 in (1, 3)):
                outputs[1].append(curNum)
                zero = False
            if (bit[inputsToPorts[a2]] + bit[inputsToPorts[b2]] + carry1 in (2, 3)):
                carry2 = 1
            else:
                carry2 = 0
            # bit 3
            if (bit[inputsToPorts[a3]] + bit[inputsToPorts[b3]] + carry2 in (1, 3)):
                outputs[2].append(curNum)
                zero = False
            if (bit[inputsToPorts[a3]] + bit[inputsToPorts[b3]] + carry2 in (2, 3)):
                carry3 = 1
            else:
                carry3 = 0
            # bit 4
            if (bit[inputsToPorts[a4]] + bit[inputsToPorts[b4]] + carry3 in (1, 3)):
                outputs[3].append(curNum)
                zero = False
            if (bit[inputsToPorts[a4]] + bit[inputsToPorts[b4]] + carry3 in (2, 3)):
                carry4 = 1
            else:
                carry4 = 0
            # zero
            if (zero):
                outputs[4].append(curNum)
            # carryout
            if carry4 == 1:
                outputs[5].append(curNum)
            # overflow
            if ((bit[inputsToPorts[a4]] == 1 and bit[inputsToPorts[b4]] == 1 and carry3 == 0) or (bit[inputsToPorts[a4]] == 0 and bit[inputsToPorts[b4]] == 0 and bit[inputsToPorts[a3]] + bit[inputsToPorts[b3]] + carry2 in (2, 3))):
                outputs[6].append(curNum)
        # subtraction
        if (bit[8] == 0 and bit[9] == 0 and bit[10] == 1):
            zero = True
            # bit 1
            carry1 = 0
            invB = [bit[inputsToPorts[b1]] ^ 1, bit[inputsToPorts[b2]] ^ 1, bit[inputsToPorts[b3]] ^ 1, bit[inputsToPorts[b4]] ^ 1]
            adding = True
            for i in range(len(invB)):
                if adding:
                    if (invB[i] == 0):
                        adding = False
                    invB[i] ^= 1
            if (bit[inputsToPorts[a1]] ^ invB[0] == 1):
                outputs[0].append(curNum)
                zero = False
            elif (bit[inputsToPorts[a1]] + invB[0] == 2):
                carry1 = 1
            # bit 2
            if (bit[inputsToPorts[a2]] + invB[1] + carry1 in (1, 3)):
                outputs[1].append(curNum)
                zero = False
            if (bit[inputsToPorts[a2]] + invB[1] + carry1 in (2, 3)):
                carry2 = 1
            else:
                carry2 = 0
            # bit 3
            if (bit[inputsToPorts[a3]] + invB[2] + carry2 in (1, 3)):
                outputs[2].append(curNum)
                zero = False
            if (bit[inputsToPorts[a3]] + invB[2] + carry2 in (2, 3)):
                carry3 = 1
            else:
                carry3 = 0
            # bit 4
            if (bit[inputsToPorts[a4]] + invB[3] + carry3 in (1, 3)):
                outputs[3].append(curNum)
                zero = False
            if (bit[inputsToPorts[a4]] + invB[3] + carry3 in (2, 3)):
                carry4 = 1
            else:
                carry4 = 0
            # zero
            if (zero):
                outputs[4].append(curNum)
            # carryout
            if carry4 == 1:
                outputs[5].append(curNum)
            # overflow
            if ((bit[inputsToPorts[a4]] == 1 and invB[3] == 1 and carry3 == 0) or (bit[inputsToPorts[a4]] == 0 and invB[3] == 0 and bit[inputsToPorts[a3]] + invB[2] + carry2 in (2, 3))):
                outputs[6].append(curNum)
        # xor
        if (bit[8] == 0 and bit[9] == 1 and bit[10] == 0):
            if (bit[inputsToPorts[a1]] ^ bit[inputsToPorts[b1]]):
                outputs[0].append(curNum)
            if (bit[inputsToPorts[a2]] ^ bit[inputsToPorts[b2]]):
                outputs[1].append(curNum)
            if (bit[inputsToPorts[a3]] ^ bit[inputsToPorts[b3]]):
                outputs[2].append(curNum)
            if (bit[inputsToPorts[a4]] ^ bit[inputsToPorts[b4]]):
                outputs[3].append(curNum)
        # slt
        if (bit[8] == 0 and bit[9] == 1 and bit[10] == 1):
            if (bit[inputsToPorts[b4]] > bit[inputsToPorts[a4]] or (bit[inputsToPorts[b4]] + bit[inputsToPorts[a4]] == 2 and (bit[inputsToPorts[b3]] > bit[inputsToPorts[a3]] or (bit[inputsToPorts[b3]] + bit[inputsToPorts[a3]] == 2 and (bit[inputsToPorts[b2]] > bit[inputsToPorts[a2]] or (bit[inputsToPorts[b2]] + bit[inputsToPorts[a2]] == 2 and (bit[inputsToPorts[b1]] > bit[inputsToPorts[a1]]))))))):
                outputs[0].append(curNum)
        # and
        if (bit[8] == 1 and bit[9] == 0 and bit[10] == 0):
            if (bit[inputsToPorts[a1]] and bit[inputsToPorts[b1]]):
                outputs[0].append(curNum)
            if (bit[inputsToPorts[a2]] and bit[inputsToPorts[b2]]):
                outputs[1].append(curNum)
            if (bit[inputsToPorts[a3]] and bit[inputsToPorts[b3]]):
                outputs[2].append(curNum)
            if (bit[inputsToPorts[a4]] and bit[inputsToPorts[b4]]):
                outputs[3].append(curNum)
        # or
        if (bit[8] == 1 and bit[9] == 0 and bit[10] == 1):
            if not(bit[inputsToPorts[a1]] and bit[inputsToPorts[b1]]):
                outputs[0].append(curNum)
            if not(bit[inputsToPorts[a2]] and bit[inputsToPorts[b2]]):
                outputs[1].append(curNum)
            if not(bit[inputsToPorts[a3]] and bit[inputsToPorts[b3]]):
                outputs[2].append(curNum)
            if not(bit[inputsToPorts[a4]] and bit[inputsToPorts[b4]]):
                outputs[3].append(curNum)
        # nor
        if (bit[8] == 1 and bit[9] == 1 and bit[10] == 0):
            if not(bit[inputsToPorts[a1]] or bit[inputsToPorts[b1]]):
                outputs[0].append(curNum)
            if not(bit[inputsToPorts[a2]] or bit[inputsToPorts[b2]]):
                outputs[1].append(curNum)
            if not(bit[inputsToPorts[a3]] or bit[inputsToPorts[b3]]):
                outputs[2].append(curNum)
            if not(bit[inputsToPorts[a4]] or bit[inputsToPorts[b4]]):
                outputs[3].append(curNum)
        # or
        if (bit[8] == 1 and bit[9] == 1 and bit[10] == 1):
            if (bit[inputsToPorts[a1]] or bit[inputsToPorts[b1]]):
                outputs[0].append(curNum)
            if (bit[inputsToPorts[a2]] or bit[inputsToPorts[b2]]):
                outputs[1].append(curNum)
            if (bit[inputsToPorts[a3]] or bit[inputsToPorts[b3]]):
                outputs[2].append(curNum)
            if (bit[inputsToPorts[a4]] or bit[inputsToPorts[b4]]):
                outputs[3].append(curNum)
    return outputs

if __name__ == '__main__':
    x = genALU4bitMT()
    print(x)
    print(len(x))
    print(sum(len(y) for y in x))
