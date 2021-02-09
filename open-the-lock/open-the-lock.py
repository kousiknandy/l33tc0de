from typing import List
from collections import deque

class Solution:
    def nextstate(self, current):
        for i, c in enumerate(current):
            yield current[:i] + str((int(c)+1) % 10) + current[i+1:]
            yield current[:i] + str((int(c)-1) % 10) + current[i+1:]
            
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        if target == start: return 0
        if start in deadends: return -1
        bfsq = deque()
        visited = {}
        bfsq.append((start, 0))
        while len(bfsq) > 0:
            current, steps = bfsq.popleft()
            if current in visited: continue
            visited[current] = True
            if current == target: return steps
            for nextstep in self.nextstate(current):
                if nextstep in deadends: continue
                if nextstep in visited: continue
                bfsq.append((nextstep, steps+1))
        return -1
        


S = Solution()
# for n in S.nextstate("90"):
#     print(n, end=" ")
print(S.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(S.openLock(deadends = ["8888"], target = "0009"))
print(S.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
