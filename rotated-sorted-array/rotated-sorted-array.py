from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        doublenums = nums[:] + nums[:]
        l, r = 0, len(nums)-1
        print(nums[l:r+1])
        while r >= l:
            m = l + (r - l)//2
            print(">", l, m, r, end=" ")
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            if l < len(nums) and r > 0:
                if nums[l] > target or nums[r] < target:
                    break
        l, r = len(nums) // 2, len(nums) + len(nums) // 2 - 1
        print("\n", doublenums[l:r+1])
        while r >= l:
            m = l + (r - l)//2
            print(">>", l, m, r, end=" ")
            if doublenums[m] == target:
                return m if m < len(nums) else m - len(nums)
            if doublenums[m] < target:
                l = m + 1
            else:
                r = m - 1
            #if nums[l] > nums[m] or nums[r] < nums[m]:
            #    break
        return -1

S = Solution()
print(S.search(nums = [4,5,6,7,0,1,2], target = 0))
print(S.search(nums = [4,5,6,7,0,1,2], target = 5))
print(S.search(nums = [4,5,6,7,0,1,2], target = 3))
print(S.search(nums = [1], target = 1))
print(S.search(nums = [1], target = 2))
print(S.search(nums = [1, 2, 3, 4, 5, 6, 7, 8], target = 1))
print(S.search([4,5,6,7,8,1,2,3],8))
print(S.search([5,1,2,3,4],1))
print(S.search([4,5,6,7,8,9,1,2,3], 1))
