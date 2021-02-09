from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        if len(nums) == 2: 
            nums[0], nums[1] = nums[1], nums[0]
            return
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        j = len(nums)
                        nums[i:j] = sorted(nums[i:j])
                        return
        nums.reverse()


S = Solution()
nums = [1, 2, 3]
S.nextPermutation(nums)
print(nums)
nums = [1, 3, 2]
S.nextPermutation(nums)
print(nums)
