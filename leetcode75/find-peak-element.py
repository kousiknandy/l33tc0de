class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if (m >= len(nums) - 1 or nums[m] > nums[m + 1]) and (
                m <= 0 or nums[m] > nums[m - 1]
            ):
                return m
            if nums[m] > nums[m+1]:
                r = m - 1
            else:
                l = m + 1
        return l
