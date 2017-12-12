from collections import deque
from eqNodes import VariableNode, UnaryNode, BinaryNode

def calcLatency(head):
	'''
	Calculates the latency of the logic tree based on the depth of binary and unary nodes
	'''
	if (head is None or isinstance(head, VariableNode)):
		return 0
	nodes = [calcLatency(head.arg1)]
	extra = 0
	if (isinstance(head, BinaryNode)):
		nodes.append(calcLatency(head.arg2))
		extra = 1
	return 1 + max(nodes) + extra


def calcArea(head):
	'''
	Calculates the area of the logic tree based on the number of binary and unary nodes
	'''
	area = 0
	q = deque()
	q.append(head)
	while len(q) > 0:
		curNode = q.popleft()
		if (isinstance(curNode, VariableNode)):
			continue
		q.append(curNode.arg1)
		if (isinstance(curNode, UnaryNode)):
			area += 1
		elif (isinstance(curNode, BinaryNode)):
			q.append(curNode.arg2)
			area += 3
	return area

def calcAreaMultiHelper(head, seen):
	if (isinstance(head, VariableNode)):
		return 0
	if (repr(head) in seen):
		return 0
	area = 0
	area += calcAreaMultiHelper(head.arg1, seen) + 1
	if (isinstance(head, BinaryNode)):
		area += calcAreaMultiHelper(head.arg2, seen) + 1
	seen[repr(head)] = area
	return area

def calcAreaMultiHead(heads):
	area = 0
	seen = {}
	for head in heads:
		area += calcAreaMultiHelper(head, seen)
	return area

