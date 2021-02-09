from typing import List
from collections import deque

class Solution:
    def previous_hops(self, curr, a, b, banned, lastjump):
        if not (curr - a in banned):
            if curr - a >= 0: yield curr - a, True
        if lastjump and not (curr + b in banned):
            if curr + b <= 2000: yield curr + b, False
            
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        banned = {x: True for x in forbidden}
        hops   = {x: 0}
        bfsq   = deque()
        bfsq.append((x, 0, 0, True))
        d_s    = 0
        while len(bfsq) > 0:
            curpos, step, _, jf = bfsq.popleft()
            if curpos == 0:
                return step
            for p, f in self.previous_hops(curpos, a, b, banned, True):
                if p not in hops:
                    hops[p] = step + 1
                    bfsq.append((p, step+1, curpos, f))
                    if step > d_s:
                        print()
                        d_s = step
                    print((p,step+1,curpos), end=",")
        return -1

S = Solution() 
print(S.minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))  # 3
print(S.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))  # -1 
print(S.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7)) # 2
print(S.minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98],29,98,80)) # 121
