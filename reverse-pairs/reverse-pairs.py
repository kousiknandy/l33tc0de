from typing import List

class Solution:
    def paircount(self, left, right):
        count = 0
        i = 0
        for j in range(len(right)):
            print(" ", i, j, count)
            if left[i] > 2*right[j]:
                count += len(left) - i
                continue
            while i < len(left)-1:
                i += 1
                if left[i] > 2*right[j]:
                    count += len(left) - i
                    break
        return count
    
    def reversePairs(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return 0
        if l == 2:
            return 1 if nums[0] > 2*nums[1] else 0
        m = (l + 1) // 2
        left = nums[:m]
        right = nums[m:]
        print(left, right)
        count = self.paircount(sorted(left), sorted(right))
        count += self.reversePairs(left)
        count += self.reversePairs(right)
        return count

S = Solution()
# print(S.paircount([1, 4, 6, 7], [1, 2, 3]))
# print(S.paircount([7], [1, 2, 3]))
# print(S.paircount([1, 2, 3], [1, 2, 3]))
# print(S.paircount([1, 2, 3], [10]))
print(S.reversePairs([1,3,2,3,1]))  #2
print(S.reversePairs([2,4,3,5,1]))  #3
print(S.reversePairs([8, 10, 3, 9, 6, 4]))  #4
