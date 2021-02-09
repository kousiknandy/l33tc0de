from typing import List
from time import sleep

class Solution:
    def partition(self, nums, left, right):
        print(nums[left:right+1])
        if left == right:
            return left
        pvt = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < pvt:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[right] = nums[right], nums[i+1]
        return i+1

    def newidx(self, old, size):
        if old % 2 == 0: return old // 2
        return (size // 2) + ((old - 1) // 2)
    
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        midpt = 0
        while True:
            midpt = self.partition(nums, left, right)
            print(midpt, nums)
            if midpt == len(nums) // 2:
                break
            elif midpt < len(nums) // 2:
                left = midpt + 1
            else:
                right = midpt - 1
        i = 1
        j = midpt
        if len(nums) % 2: j += 1
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[j] = nums[j], nums[i]
            print(i,j)
            j += 1

S = Solution()

nums = [4, 2, 3, 7, 5, 4, 9, 6]
print(S.wiggleSort(nums))
print(nums)

nums = [4, 2, 3, 7, 5, 4, 9, 6, 3]
print(S.wiggleSort(nums))
print(nums)

nums = [4, 2, 3, 7, 5, 4, 9, 6, 8]
print(S.wiggleSort(nums))
print(nums)

nums = [4, 2, 3, 7, 5, 1, 4, 9, 6, 8]
print(S.wiggleSort(nums))
print(nums)

nums = [4, 2, 3, 4, 5, 4, 9, 4, 8]
print(S.wiggleSort(nums))
print(nums)

nums = [1,3,2,2,3,1]
print(S.wiggleSort(nums))
print(nums)

