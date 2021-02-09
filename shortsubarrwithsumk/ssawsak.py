class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l = len(A)
        mem = {}
        for offset in range(1, l+1):
            lsum = 0
            for idx in range(l):
                if (idx + offset) > l:
                    continue
                if idx == 0:
                    if (idx,offset) not in mem:
                        lsum = sum(A[idx:idx+offset])
                        mem[(idx,offset)] = lsum
                    else:
                        lsum = mem[(idx,offset)]
                        print("cached")
                else:
                    lsum += A[idx+offset-1]
                #print(lsum)
                mem[(idx,offset)] = lsum
                if lsum >= K:
                    return offset
                lsum -= A[idx]
                mem[(idx+1,offset)] = lsum
                #print(lsum)
        return -1

S = Solution()
print(S.shortestSubarray([5, -2, 6, 7, -9], 8))
