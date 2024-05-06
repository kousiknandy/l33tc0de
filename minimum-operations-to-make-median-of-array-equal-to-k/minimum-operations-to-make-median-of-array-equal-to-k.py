class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        m = len(nums) // 2
        o = abs(k - nums[m])
        for i in range(m-1, -1, -1):
            if nums[i] <= k: break
            o += abs(k - nums[i])
        for i in range(m+1, len(nums)):
            if nums[i] >= k: break
            o += abs(k - nums[i])
        return o
