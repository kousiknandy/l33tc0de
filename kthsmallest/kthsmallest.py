class max_heap():
    def __init__(self, maxsz):
        x = 1
        while x-1 < maxsz:
            x *= 2
        self.heap = [0 for _ in range(x-1)]
        self.size = 0
        self.maxsz = maxsz

    def _parent(self, n):
        return (n-1)//2 if n > 1 else 0

    def _children(self, n):
        yield 2*n + 1
        yield 2*n + 2

    def pushme(self, val):
        if self.size < self.maxsz:
            self.heap[self.size] = val
            idx = self.size
            while val > self.heap[self._parent(idx)]:
                self.heap[idx], self.heap[self._parent(idx)] = \
                    self.heap[self._parent(idx)], self.heap[idx]
                idx = self._parent(idx)
            self.size += 1
            return val
        else:
            if val > self.heap[0]:
                return val
            pmax = self.heap[0]
            self.heap[0] = val
            p = 0
            while True:
                if p >= self.maxsz//2:
                    return pmax
                cl = self.heap[2*p+1]
                cr = self.heap[2*p+2]
                if val >= cl and val >= cr:
                    return pmax
                if cl >= cr:
                    p1 = 2*p + 1
                else:
                    p1 = 2*p + 2
                self.heap[p], self.heap[p1] = \
                    self.heap[p1], self.heap[p]
                p = p1

    def get_max(self):
        return self.heap[0] if self.size > 0 else None

    def __repr__(self):
        return str(self.size) + ", " + str(self.heap)
    
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        h = max_heap(B)
        print(sorted(A))
        for i in A:
            h.pushme(i)
            print(i, h)
        return h.get_max()

S = Solution()
x = S.kthsmallest([3, 5, 2, 6, 4], 3) #4
x = S.kthsmallest([3, 5, 2, 6, 4, 8, 1], 4) #4
x = S.kthsmallest([ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ], 1) #18
x = S.kthsmallest([ 84, 93, 87, 32, 61, 59, 4, 6, 47, 44, 13, 68, 6, 40, 47, 55, 86, 44, 3, 6, 84, 86, 99, 30, 20, 64, 24, 49, 67, 85 ], 12)

