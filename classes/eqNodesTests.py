from eqNodes import VariableNode, UnaryNode, BinaryNode


def testVariableNode():
    a = VariableNode(name='a')
    if a.eval({'a': True}) is True:
        print('Variable Node Test Passed')
    else:
        print('Variable Node Test Failed!')

testVariableNode()
