class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        maxi = 0
        maxj = 0
        i = 0
        j = 0
        max = -1
        sum = 0
        p = False
        for idx, n in enumerate(A):
            if n >= 0:
                sum += n
                j = idx
                p = True
            if max < sum:
                max = sum
                maxi = i
                maxj = j
            if max == sum:
                if (maxj - maxi) < (j - i):
                    maxi = i
                    maxj = j
                if (maxj - maxi) == (j - i):
                    if maxi > i:
                        maxi = i
                        maxj = j
            if n < 0:
                sum = 0
                i = j = idx+1
        return A[maxi:maxj+1] if p else []

S = Solution()
print(S.maxset([3, 2, 1, -1, 4, 2]))
print(S.maxset([ 2]))
print(S.maxset([3, 2, 1, -1]))
print(S.maxset([-3, -2, 1, -1, 1, 2]))
print(S.maxset([3, 2, -1, -1, 1, 2, 1, 1]))
print(S.maxset([3, 2, -1, -1,  2, 3, -1]))
print(S.maxset([-3, -2, -1, -1,  -2, -3, -1]))
      
