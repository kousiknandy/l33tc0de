from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r > l:
            m = l + (r - l)//2
            #print(">", l, m, r, end=" ")
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        #print(nums, l)
        offset = l
        l, r, sz = 0, len(nums)-1, len(nums)
        while r >= l:
            m = l + (r - l)//2
            m1 = (m + offset) % sz
            if target == nums[m1]:
                return m1
            if target < nums[m1]:
                r = m-1 
            else:
                l = m+1
        return -1
                
S = Solution()
print(S.search(nums = [4,5,6,7,0,1,2], target = 0)) #4
print(S.search(nums = [4,5,6,7,0,1,2], target = 5)) #1
print(S.search(nums = [4,5,6,7,0,1,2], target = 3)) #-1
print(S.search(nums = [1], target = 1)) #0
print(S.search(nums = [1], target = 2)) #-1
print(S.search(nums = [1, 2, 3, 4, 5, 6, 7, 8], target = 1)) #0
print(S.search([4,5,6,7,8,1,2,3],8)) #4
print(S.search([5,1,2,3,4],1)) #1
print(S.search([4,5,6,7,8,9,1,2,3], 1)) #6
