from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 1: return True
        memo = [False] * l
        for i in range(l-1, -1, -1):
            print(i,nums[i], memo)
            j = nums[i]
            if i + j >= l - 1:
                memo[i] = True
                continue
            for k in range(1, j+1):
                if memo[i + k]:
                    memo[i] = True
                    break
        return memo[0]

S = Solution()
print(S.canJump(nums = [2,3,1,1,4]))
print(S.canJump(nums = [1,2,3]))
#print(S.canJump())
