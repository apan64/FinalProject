from treeFunctions import calcLatency, calcArea
from eqNodes import VariableNode, UnaryNode, BinaryNode

def testCalcLatency():
	a = VariableNode(name='a')
	b = VariableNode(name='b')
	a_and_b = BinaryNode(fn=lambda x, y: (x and y), name='and', arg1=a, arg2=b)
	ans =  calcLatency(a_and_b)
	if (ans != 1):
		print('calcLatency test 1 failed')
	else:
		print('calcLatency test 1 passed')
	c = UnaryNode(fn = lambda x: x, name = 'nuthing', arg1 = a_and_b)
	d = BinaryNode(fn = lambda x, y: (x and y), name = 'and', arg1 = c, arg2 = a)
	ans =  calcLatency(d)
	if (ans != 3):
		print('calcLatency test 2 failed')
	else:
		print('calcLatency test 2 passed')

def testCalcArea():
	a = VariableNode(name='a')
	b = VariableNode(name='b')
	a_and_b = BinaryNode(fn=lambda x, y: (x and y), name='and', arg1=a, arg2=b)
	ans =  calcArea(a_and_b)
	if (ans != 2):
		print('calcArea test 1 failed')
	else:
		print('calcArea test 1 passed')
	c = UnaryNode(fn = lambda x: x, name = 'nuthing', arg1 = a_and_b)
	d = BinaryNode(fn = lambda x, y: (x and y), name = 'and', arg1 = c, arg2 = a)
	ans =  calcArea(d)
	if (ans != 5):
		print('calcArea test 2 failed')
	else:
		print('calcArea test 2 passed')

testCalcLatency()
testCalcArea()