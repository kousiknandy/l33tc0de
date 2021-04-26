from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        f0 = sum(n*i for n, i in zip(nums, range(len(nums))))
        maxm = f0
        # print(f0)
        for i in range(len(nums)-1, 0, -1):
            f1 = f0 + total - nums[i] * len(nums)
            if maxm < f1: maxm = f1
            f0 = f1
            # print(f0)
        return maxm

S = Solution()
print(S.maxRotateFunction(nums = [4,3,2,6]))
