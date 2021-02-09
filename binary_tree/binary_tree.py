from functools import partialmethod

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    IN, PRE, POST = 1, 2, 3
    
    def __init__(self, root):
        self.root = root

    def traverse(self, root, order):
        if not root: return None
        if order == self.IN:
            yield from self.traverse(root.left, order)
            yield root
            yield from self.traverse(root.right, order)
        elif order == self.PRE:
            raise NotImplementedError
        elif order == self.POST:
            raise NotImplementedError
        else:
            raise TypeError

    def iterative_inorder(self, root):
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                yield root
                root = root.right
        
    inorder = partialmethod(traverse, order = IN)
    preorder = partialmethod(traverse, order = PRE)
    postorder = partialmethod(traverse, order = POST)
        
n = Node(30)
l = Node(20)
r = Node(40)
n.left = l
n.right = r
l = Node(35)
r.left = l
r = Node(37)
l.right = r
t = Tree(n)

for node in t.inorder(t.root):
    print(node.val)

for node in t.iterative_inorder(t.root):
    print(node.val)
