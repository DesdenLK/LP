class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []
    
    def add_child(self, a):
        self.child.append(a)
    
    def root(self):
        return self.rt
    
    def ith_child(self, x):
        return self.child[x]
    
    def num_children(self):
        l = len(self.child)
        for node in self.child:
            l += node.num_children()
        return l


class Pre(Tree):
    def __init__(self, x):
        super().__init__(x)
    
    def preorder(self):
        R = []
        R.append(self.rt)
        for t in self.child:
            R += t.preorder()
        return R
    
