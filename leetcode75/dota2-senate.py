from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        now = deque(senate)
        later = deque()
        r,d = 0,0
        while True:
            rx,dx = False, False
            while len(now):
                x = now.popleft()
                if x == "R":
                    rx = True
                    if r > 0:
                        r -= 1
                        continue
                    d += 1
                    later.append(x)
                if x == "D":
                    dx = True
                    if d > 0:
                        d -= 1
                        continue
                    r += 1
                    later.append(x)
            if not rx: return "Dire"
            if not dx: return "Radiant"
            now = later
            later = deque()    
