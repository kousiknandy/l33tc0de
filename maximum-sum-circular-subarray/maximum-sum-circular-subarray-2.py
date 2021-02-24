from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        bmax = - (2 ** 32)
        cmax = 0
        bmin = 2 ** 32
        cmin = 0
        for a in A:
            cmax = max(cmax + a, a)
            bmax = max(bmax, cmax)
            cmin = min(cmin + a, a)
            bmin = min(bmin, cmin)
        maxsubarr = max(bmax, sum(A) - bmin)
        return maxsubarr if maxsubarr else bmax


S = Solution()
print(S.maxSubarraySumCircular([3,-1,2,-1]))  # 4
print(S.maxSubarraySumCircular([1,-2,3,-2]))  # 3
print(S.maxSubarraySumCircular([5,5,5]))      # 15
print(S.maxSubarraySumCircular([5,-3,4]))     # 9
print(S.maxSubarraySumCircular([3,-2,2,-3]))  # 3
print(S.maxSubarraySumCircular([-4,-2,-3]))   # -2
print(S.maxSubarraySumCircular([-1,-1,-1,-1,-1]))  # -1
