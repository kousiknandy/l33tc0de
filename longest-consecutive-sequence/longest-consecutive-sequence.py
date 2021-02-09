class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        frq = dict()
        max = 0
        for n in A:
            if n in frq:
                frq[n] += 1
            else:
                frq[n] = 1
            if max < frq[n]:
                max = frq[n]
                
            i = 1
            while True:
                if n+i in frq:
                    frq[n+i] += 1
                    if max < frq[n+i]:
                        max = frq[n+i]
                    i += 1
                else:
                    break
                
            i = 1
            while True:
                if n-i in frq:
                    frq[n-i] += 1
                    if max < frq[n-i]:
                        max = frq[n-i]
                    i += 1
                else:
                    break
            print(n, frq)
        return max

S = Solution()
print(S.longestConsecutive([100, 4, 200, 1, 3, 2]))
