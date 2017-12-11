class VariableNode:
    def __init__(self, name):
        self.name = name.lower()

    def eval(self, lookup):
        if self.name not in lookup:
            raise KeyError("{0} not found in {1}".format(self.name, str(lookup)))
        return lookup[self.name]
    def toString(self):
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
    def toString(self):
        return self.name + self.arg1.toString()


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
    def toString(self):
        return self.name + self.arg1.toString() + self.arg2.toString()
