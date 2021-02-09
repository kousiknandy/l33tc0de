from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        onemin, onemax, twomin = 0, 0, len(nums)-1
        while onemax <= twomin:
            if nums[onemax] == 0:
                nums[onemin], nums[onemax] = nums[onemax], nums[onemin]
                onemin += 1
                onemax += 1
            elif nums[onemax] == 1:
                onemax += 1
            elif nums[onemax] == 2:
                nums[twomin], nums[onemax] = nums[onemax], nums[twomin]
                twomin -= 1

S = Solution()
nums = [2,0,2,1,1,0]
S.sortColors(nums)
print(nums)
