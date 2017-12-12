# import plotTree

class VariableNode:
    def __init__(self, name):
        self.name = name.lower()

    def eval(self, lookup):
        if self.name not in lookup:
            raise KeyError("{0} not found in {1}".format(self.name, str(lookup)))
        return lookup[self.name]

    def __repr__(self):
        return self.name


class UnaryNode:
    def __init__(self, fn, name, arg1=None):
        self.name = name.lower()
        self.fn = fn
        self.arg1 = arg1

    def eval(self, lookup):
        if self.arg1 is None:
            raise ValueError("Arg1 should not be None")
        return self.fn(self.arg1.eval(lookup))

    def __repr__(self):
        return "{0}({1})".format(self.name, self.arg1)


class BinaryNode:
    def __init__(self, fn, name, arg1=None, arg2=None):
        self.name = name.lower()
        self.fn = fn
        self.arg1 = arg1
        self.arg2 = arg2

    def eval(self, lookup):
        if self.arg1 is None:
            raise ValueError("Arg1 should not be None")
        if self.arg2 is None:
            raise ValueError("Arg2 should not be None")
        return self.fn(self.arg1.eval(lookup), self.arg2.eval(lookup))

    def __repr__(self):
        return "{0}({1}, {2})".format(self.name, self.arg1, self.arg2)

    # def plot(self):
    #     vertices, numVertices = getVertices(self)
    #     nodesToID = {v: k for k, v in vertices.items()}
    #     plotTree.plotTree(vertices, getEdges(b_and_not_a, nodesToID), numVertices)



def getVertices(head, i=0):
    """Returns all vertices in graph as a dictionary of vertex_n : <node>"""
    vertices = {}
    if hasattr(head, 'arg1'):
        child_vertices, i = getVertices(head.arg1, i)
        vertices = merge_two_dicts(vertices, child_vertices)
    vertices = merge_two_dicts(vertices, {i: head})
    i += 1
    if hasattr(head, 'arg2'):
        child_vertices, i = getVertices(head.arg2, i)
        vertices = merge_two_dicts(vertices, child_vertices)
    return vertices, i


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def getEdges(head, nodesToID):
    edges = []
    if hasattr(head, 'arg1'):
        edges.append((nodesToID[head], nodesToID[head.arg1]))
        child_edges = getEdges(head.arg1, nodesToID)
        edges += child_edges
    if hasattr(head, 'arg2'):
        edges.append((nodesToID[head], nodesToID[head.arg2]))
        child_edges = getEdges(head.arg2, nodesToID)
        edges += child_edges
    return edges

# a = VariableNode(name='a')
# not_a = UnaryNode(fn=lambda x: not(x), name='not', arg1=a)
# b = VariableNode(name='b')
# b_and_not_a = BinaryNode(fn=lambda x, y: (x and y), name='and', arg1=b, arg2=not_a)

# b_and_not_a.plot()
