from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumcache = defaultdict(int)
        sumcache[0] = 1
        cumulation = 0
        counter = 0
        for n in nums:
            cumulation += n
            counter += sumcache[cumulation - k]
            sumcache[cumulation] += 1
            #print("(",n,")",cumulation, counter, ":", sumcache)
        return counter

S = Solution()
print(S.subarraySum([1, 2, 3, 1, 5], 6))
