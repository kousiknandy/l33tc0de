from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maxlen = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    maxlen = max(maxlen, dp[i])
        return maxlen

S = Solution()
print(S.lengthOfLIS([10,9,2,5,3,7,101,18]))

