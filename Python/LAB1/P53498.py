class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []
    
    def __iter__(self):
        yield self.rt
        breath = self.child
        while breath:
            node = breath.pop(0)
            yield node.rt
            breath += node.child
    
    def addChild(self, a):
        self.child.append(a)
    
    def root(self):
        return self.rt
    
    def ithChild(self, x):
        return self.child[x]
    
    def num_children(self):
        l = len(self.child)
        for node in self.child:
            l += node.num_children()
        return l