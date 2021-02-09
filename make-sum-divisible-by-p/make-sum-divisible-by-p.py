from typing import List
from collections import defaultdict

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        print()
        sumcache  = {0: -1}
        cumulant  = 0
        getridof  = sum(nums) % p
        res       = len(nums)
        if not getridof: return 0
        print(getridof, res)
        for i, n in enumerate(nums):
            cumulant += n
            cumulant %= p
            sumcache[cumulant] = i
            diff = (cumulant - getridof) % p
            print(i, n, cumulant, diff, sumcache, sumcache.get(diff,-1), res)
            if diff in sumcache:
                res = min(res, i - sumcache[diff])
        return res if res < len(nums) else -1


S = Solution()
print(S.minSubarray(nums = [6,3,5,2], p = 9))
print(S.minSubarray(nums = [3,1,4,2], p = 6))
print(S.minSubarray(nums = [1,2,3], p = 6))
print(S.minSubarray(nums = [1,2,3], p = 3))
print(S.minSubarray(nums = [1,2,3], p = 7))
print(S.minSubarray(nums = [1000000000,1000000000,1000000000], p = 3))
print(S.minSubarray(nums = [1], p = 1))
print(S.minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148))
print(S.minSubarray([17,6,22,31,25,4,18,32,18,26,2,31,26,8,12,2],142))
