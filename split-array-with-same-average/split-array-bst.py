from typing inport List

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root


    def minimum(self, root=None):
        curr = root if root else self.root
        while curr.left:
            curr = curr.left
        return curr

    def maximum(self, root=None):
        curr = root if root else self.root
        while curr.right:
            curr = curr.right
        return curr
    
    def hunt(self, val, root=None, delta=True):
        curr = root if root else self.root
        parent = curr
        while curr:
            if curr.val > val:
                if curr.left:
                    maxm = self.maximum(curr.left)
                    if maxm.val < val:
                        if delta:
                            break
                    else:
                        parent = curr
                        curr = curr.left
                        continue
            if curr.val < val:
                if curr.right:
                    minm = self.minimum(curr.right)
                    if minm.val > val:
                        if not delta:
                            break
                    else:
                        parent = curr
                        curr = curr.right
                        continue
            if curr.val == val:
                break
        
