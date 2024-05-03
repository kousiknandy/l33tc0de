class Solution(object):
    def seeksum(self, nums, cursum, target):
        c = 0
        if len(nums) == 1:
            if cursum + nums[0] == target: c += 1
            if cursum - nums[0] == target: c += 1
            return c
        if cursum + sum(nums) < target: return c
        if cursum - sum(nums) > target: return c
        c += self.seeksum(nums[1:], cursum+nums[0], target)
        c += self.seeksum(nums[1:], cursum-nums[0], target)
        return c

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.seeksum(sorted(nums,reverse=True), 0, target)
