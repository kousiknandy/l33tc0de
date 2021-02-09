from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        if r <= 3: return target in nums
        eqelem = None
        if nums[l] == nums[r]:
            eqelem = nums[l]
            while nums[l] == eqelem:
                l += 1
            while nums[r] == eqelem:
                r -= 1
        if eqelem is not None and nums[r] > eqelem:
            pivot = r + 1
        else:
            if l == r:
                if nums[l] > nums[l+1]:
                    l += 1
            while r > l:
                m = (r + l) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            pivot = l
        print(pivot)
        l = 0
        r = len(nums) - 1
        while r >= l:
            m = (r + l) // 2
            m1 = (m + pivot) % len(nums)
            print(l, m, m1, r)
            if target == nums[m1]: return True
            if target < nums[m1]:
                r = m - 1
            else:
                l = m + 1
        return False


S = Solution()
print(S.search([7, 8, 9, 9, 10, 11, 12, 3, 3, 4, 5], 8))
print(S.search([2,2,2, 3, 2,2,2], 3))
print(S.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))
print(S.search([1,0,1,1,1], 0))
print(S.search([1,1,2,2,1], 2))
