from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxarr = [None] * 3
        for n in nums:
            print(n, end=" ")
            for i in [0, 1, 2]:
                if (maxarr[i] is None) or (n > maxarr[i]):
                    p = maxarr[i]
                    maxarr[i] = n
                    n = p
                elif n == maxarr[i]:
                    break
            print(maxarr)
        return maxarr[2] if maxarr[2] is not None else maxarr[0]


S = Solution()
print(S.thirdMax([2, 5, 6, 8, 3, 9])) # 6
print(S.thirdMax([3, 2, 1])) # 1
print(S.thirdMax([1, 2])) # 2
print(S.thirdMax([2, 2, 3, 1])) # 1
