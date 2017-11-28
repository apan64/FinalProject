class VariableNode:
    def __init__(self, name):
        self.name = name.lower()

    def eval(self, lookup):
        if self.name not in lookup:
            raise KeyError("{0} not found in {1}".format(self.name, str(lookup)))
        return lookup[self.name]


class UnaryNode:
    def __init__(self, fn, name, arg1=None):
        self.name = name.lower()
        self.fn = fn
        self.arg1 = arg1

    def eval(self, lookup):
        if (arg1 is None):
            raise ValueError("Arg1 should not be None")
        return self.fn(arg1.eval(lookup))


class BinaryNode:
    def __init__(self, fn, name, arg1=None, arg2=None):
        self.name = name.lower()
        self.fn = fn
        self.arg1 = arg1
        self.arg2 = arg2

    def eval(self, lookup):
        if (arg1 is None):
            raise ValueError("Arg1 should not be None")
        if (arg2 is None):
            raise ValueError("Arg2 should not be None")
        return self.fn(arg1.eval(lookup), arg2.eval(lookup))
