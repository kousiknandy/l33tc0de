from collections import deque

class Solution:
    def next_step(self, x, cx, y, cy):
        yield 0, cy # empty x
        yield cx, 0 # empty y
        if x > cx:
            yield x, cy # fill x
        if y > cy:
            yield cx, y # fill y
        if cx > 0:
            yc = y - cy
            if yc > 0:
                if yc >= cx:
                    yield 0, cy+cx # empty x into y
                else:
                    yield cx - yc, y # pour x to y till full
        if cy > 0:
            xc = x - cx
            if xc > 0:
                if xc >= cy:
                    yield cx+cy, 0 # empty y into x
                else:
                    yield x, cy - xc # pour y into x till full
        
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        cx = cy = 0
        bfsq = deque()
        known_state = {(cx, cy): True}
        bfsq.append((cx,cy))
        while len(bfsq) > 0:
            cx, cy = bfsq.popleft()
            if cx == z or cy == z or cx+cy == z: return True
            for nx, ny in self.next_step(x, cx, y, cy):
                if nx == z or ny == z or nx+ny == z: return True
                if (nx, ny) not in known_state:
                    known_state[(nx, ny)] = True
                    bfsq.append((nx, ny))
        return False
    
S = Solution()
print(S.canMeasureWater(x = 3, y = 5, z = 4)) # True
print(S.canMeasureWater(x = 2, y = 6, z = 5)) # False
