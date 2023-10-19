class Solution:
    def divide_min(self, l, r):
        if r - l <= 3: return min(self.nums[l:r+1])
        m = (l + r) // 2
        if self.nums[l] < self.nums[m]:
            if self.nums[m] < self.nums[r]: return self.nums[l]
            l = m
        else: r = m
        return self.divide_min(l, r)

    def findMin(self, nums: List[int]) -> int:
        self.nums = nums
        return self.divide_min(0, len(nums)-1)
