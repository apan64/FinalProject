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


testVariableNode1()
testVariableNode2()
testUnaryNode1()
