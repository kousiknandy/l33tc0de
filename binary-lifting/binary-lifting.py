import random

class Node:
    def __init__(self, value):
        self.value = value
        self.adjacency = []
        self.parent = None

    def children(self):
        yield from self.adjacency

    def __repr__(self):
        s = str(self.value) + "("
        for c in self.children():
            s += str(c.value) + " "
        s += ")"
        return s
        
class Tree:
    def __init__(self, root):
        self.root = root

    def add_edge(self, node, parent):
        node.parent = parent
        parent.adjacency.append(node)

    def dfs(self, node, parent, depth):
        #print(depth, node)
        yield node
        for child in node.children():
            self.dfs(child, node, depth+1) 

    def bfs(self, root):
        bfs_q = [(root, 0)]
        while len(bfs_q) > 0:
            node, depth = bfs_q.pop(0)
            #print(depth, node)
            yield node
            bfs_q.extend([(x, depth+1) for x in node.children()])
            #print(bfs_q)
            
a, b, c, d, e, f, g = [Node(chr(ord('a')+_)) for _ in range(7)]
print(a, b, c, d, e, f, g)

t = Tree(a)
t.add_edge(b, a)
t.add_edge(c, a)
t.add_edge(d, a)
t.add_edge(e, b)
t.add_edge(f, b)
t.add_edge(g, d)
print(a, b, c, d, e, f, g)
nodes = t.dfs(a, a, 0)
print(nodes)

t.bfs(a)

