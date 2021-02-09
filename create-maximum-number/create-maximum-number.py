from typing import List

class Solution:
    def intvalue(self, nums: List[int]) -> int:
        value = 0
        for v in nums:
            value = value * 10 + v
        return value

    def formlargest(self, nums: List[int], k: int) -> List[int]:
        res = []
        idx = 0
        length = len(nums)
        if length < k:
            return None
        while k:
            mx = max(range(idx,length-(k-1)), key=nums.__getitem__)
            yield nums[mx]
            idx = mx+1
            k -= 1

    def mergemaxes(self, nums1: List[int], nums2: List[int], k: int, i: int) -> List[int]:
        a = self.formlargest(nums1, i)
        b = self.formlargest(nums2, k-i)
        res = []
        try:
            va = next(a)
        except StopIteration as e:
            res.extend(b)
            return res
        try:
            vb = next(b)
        except StopIteration as e:
            res.append(va)
            res.extend(a)
            return res
        while len(res) < k:
            if va > vb:
                res.append(va)
                try:
                    va = next(a)
                except StopIteration as e:
                    res.append(vb)
                    res.extend(b)
                    break
            elif va < vb:
                res.append(vb)
                try:
                    vb = next(b)
                except StopIteration as e:
                    res.append(va)
                    res.extend(a)
                    break
            else:
                
        return res
        
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        maxnums = []
        for i in range(k):
            if i > l1 or k-i > l2:
                continue
            res = self.mergemaxes(nums1, nums2, k, i)
            maxnums.append(res)
        print(maxnums)
        return max(maxnums, key=self.intvalue)
        


S = Solution()
# print(list(S.formlargest([3, 6, 9, 4, 2, 7, 3, 1], 8)))
# print(S.formlargest([3, 6, 9, 4, 2, 7, 3, 1], 7))
# print(list(S.formlargest([3, 6, 9, 4, 2, 7, 3, 1], 3)))
# print(list(S.formlargest([2,5,4,3], 4)))
# print(S.mergemaxes([3, 6, 9, 4, 2, 7, 3, 1], [2, 5, 4, 3], 7, 3))
# print(list(S.formlargest([3, 6, 9, 4, 2, 7, 3, 1], 5)))
# print(list(S.formlargest([2,5,4,3], 2)))
# print(S.mergemaxes([3, 6, 9, 4, 2, 7, 3, 1], [2, 5, 4, 3], 7, 5))
# print(S.mergemaxes([3, 6, 9, 4, 2, 7, 3, 1], [2, 5, 4, 3], 3, 0))
# print(S.mergemaxes([3, 6, 9, 4, 2, 7, 3, 1], [2, 5, 4, 3], 3, 3))

#print(S.maxNumber([3, 6, 9, 4, 2, 7, 3, 1], [2, 5, 4, 3], 4))
print(S.maxNumber([6,7], [6,0,4], 5))
