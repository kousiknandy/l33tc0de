from typing import List

class Solution:
    def leftboundary(self, prefixsum):
        total = prefixsum[-1]
        target = total // 3
        l, r = 0, len(prefixsum)-1
        while prefixsum[l] <= target:
            l += 1
        return l
        while l < r:
            m = (l + r) // 2
            if prefixsum[m] < target:
                l = m 
            elif prefixsum[m] > target:
                r = m - 1
            else:
                l = m
                break
        return l
            
    def waysToSplit(self, nums: List[int]) -> int:
        prefixsum = [0] * len(nums)
        ways = 0
        for i,n in enumerate(nums):
            prefixsum[i] = (prefixsum[i-1] if i > 0 else 0) + n
        leftmax = self.leftboundary(prefixsum)
        for rightwall in range(2, len(nums)):
            for leftwall in range(1, min(leftmax, rightwall)+1):
                left  = prefixsum[leftwall-1]
                mid   = prefixsum[rightwall-1] - prefixsum[leftwall-1]
                right = prefixsum[-1] - prefixsum[rightwall-1]
                print(leftwall, rightwall, len(nums)-1)
                print("{}({}) {}({}) {}({})".format(nums[:leftwall], left,
                                                    nums[leftwall:rightwall], mid,
                                                    nums[rightwall:], right))
                if left <= mid <= right:
                    ways += 1
        return ways

S = Solution()
print(S.waysToSplit([1,1,1]))  # 1
print(S.waysToSplit([1,2,2,2,5,0]))  # 3
print(S.waysToSplit([3,2,1]))  # 0
