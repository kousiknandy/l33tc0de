class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        uset = dict()
        m = 0
        for n in A:
            if n in uset:
                continue
            uset[n] = 1
            m = max(m, uset[n])
            if n+1 in uset:
                uset[n] += uset[n+1]
                m = max(m, uset[n])
            i = 1
            while True:
                if n-i in uset:
                    uset[n-i] += uset[n]
                    m = max(m, uset[n-i])
                    i += 1
                else:
                    break
            print(uset)
        return m

S = Solution()
print(S.longestConsecutive([100, 4, 200, 1, 3, 2]))  #4
print(S.longestConsecutive([ -6, -4, -5, -2, -3 ]))  #5

