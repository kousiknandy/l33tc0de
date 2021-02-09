from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = sorted(citations, reverse=True)
        hindex = 0
        for idx, n in enumerate(s):
            if n >= idx+1:
                hindex += 1
            else:
                break
        return hindex

S = Solution()
print(S.hIndex([1])) # 1
print(S.hIndex([1, 1, 1])) # 1
print(S.hIndex([1, 2, 3, 4])) # 2
print(S.hIndex([3,0,6,1,5]))  # 3
