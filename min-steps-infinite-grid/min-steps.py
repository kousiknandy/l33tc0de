import itertools

def dist(a1, b1, a2, b2):
    x = abs(a1 - a2)
    y = abs(b1 - b2)
    return x if x > y else y

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        d = 0
        if len(A) == 0:
            return 0
        a1 = A[0]
        b1 = B[0]
        for (a, b) in zip(A, B):
            d += dist(a, b, a1, b1)
            a1 = a
            b1 = b
        return d

S = Solution()
print(S.coverPoints([0, 1, 1], [0, 1, 2]))


