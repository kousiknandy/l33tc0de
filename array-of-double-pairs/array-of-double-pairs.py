from typing import List
from collections import defaultdict

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        halfx = defaultdict(int)
        onex  = defaultdict(int)
        twox  = defaultdict(int)
        for a in arr:
            onex[a] += 1
            if onex[2*a] or halfx[2*a]:
                twox[a] += 1
                halfx[2*a] += 1
            if a % 2 == 0 and (onex[a//2] or twox[a//2]):
                halfx[a] += 1
                twox[a//2] += 1
        candidates = sorted([x for x in twox.keys() if twox[x]])
        print(halfx, onex, twox, candidates, sep="\n")
        for c in candidates:
            if onex[c]:
                onex[c] -= 1
            else:
                continue
            if onex[2*c]:
                onex[2*c] -= 1
            else:
                return False
        for c in onex:
            if onex[c]: return False
        return True
        
S = Solution()
print(S.canReorderDoubled([1,4,2,8]))           # True
print(S.canReorderDoubled(arr = [4,-2,2,-4]))   # True
print(S.canReorderDoubled([1,2,4,16,8,4]))      # False
print(S.canReorderDoubled([3,1,3,6]))           # False
print(S.canReorderDoubled([2,1,2,6]))           # False
print(S.canReorderDoubled([0,0,0,0,0,0]))       # True
