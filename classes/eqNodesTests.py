from eqNodes import VariableNode, UnaryNode, BinaryNode


def testVariableNode1():
    a = VariableNode(name='a')
    if a.eval({'a': True}) is True:
        print('Variable Node Test 1 Passed')
    else:
        print('Variable Node Test 1 Failed!')


def testVariableNode2():
    a = VariableNode(name='a')
    if a.eval({'a': False}) is False:
        print('Variable Node Test 2 Passed')
    else:
        print('Variable Node Test 2 Failed!')


def testUnaryNode1():
    a = VariableNode(name='a')
    not_a = UnaryNode(fn=lambda x: not(x), name='not', arg1=a)
    if not_a.eval({'a': True}) is False:
        print('Unary Node Test 1 Passed')
    else:
        print('Unary Node Test 1 Failed!')


def testBinaryNode1():
    a = VariableNode(name='a')
    b = VariableNode(name='b')
    a_and_b = BinaryNode(fn=lambda x, y: (x and y), name='and', arg1=a, arg2=b)

    if a_and_b.eval({'a': True, 'b': True}) is True:
        print('Binary Node Test 1 Passed')
    else:
        print('Binary Node Test 1 Failed!')


def testBinaryNode2():
    a = VariableNode(name='a')
    not_a = UnaryNode(fn=lambda x: not(x), name='not', arg1=a)
    b = VariableNode(name='b')
    b_and_not_a = BinaryNode(fn = lambda x, y: (x and y), name='and', arg1=b, arg2=not_a)

    if b_and_not_a.eval({'a': True, 'b': True}) is False:
        print('Unary Node Test 1 Passed')
    else:
        print('Unary Node Test 1 Failed!')

testVariableNode1()
testVariableNode2()
testUnaryNode1()
testBinaryNode1()
testBinaryNode2()
