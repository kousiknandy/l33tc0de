from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.size   = n
        self.binary_lift()
        
    def binary_lift(self):
        depth = self.size.bit_length()
        liftcache = [[-1] * depth for _ in range(self.size)]
        # liftcache[i][j] = 2^j parent of i
        for i in range(self.size): liftcache[i][0] = self.parent[i]
        for j in range(1, depth):
            for i in range(self.size):
                liftcache[i][j] = liftcache[liftcache[i][j-1]][j-1] if liftcache[i][j-1] != -1 else -1
        #for l in liftcache: print(l)
        self.liftcache = liftcache

    def getKthAncestor_bruteforce(self, node: int, k: int) -> int:
        parent = node
        while k > 0:
            parent = self.parent[parent]
            if parent == -1: break
            k -= 1
        return parent

    def binbits(self, n):
        while n > 0:
            msb = n.bit_length() - 1
            yield msb
            n -= 2 ** msb

    def getKthAncestor_binarylift(self, node: int, k: int) -> int:
        parent = node
        for p in self.binbits(k):
            parent = self.liftcache[parent][p]
            if parent == -1: break
        return parent

    getKthAncestor = getKthAncestor_binarylift

T = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(T.getKthAncestor(3,1),   # 1
      T.getKthAncestor(5,2),   # 0
      T.getKthAncestor(6,3),   # -1
      )


T = TreeAncestor(16, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 11, 11, 8, 13])
#                      0  1  2  3  4  5  6  7  8  9  0  1   2   3  4   5
print(T.getKthAncestor(15,5),   # 0
      T.getKthAncestor(15,3),   # 4
      T.getKthAncestor(15,15),   # 4
      )
