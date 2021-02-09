from collections import deque

class Solution:
    def next_points(self, sx: int, sy: int, tx: int, ty: int) -> (int, int):
        nx, ny = sx, sx + sy
        if ty >= ny: yield nx, ny
        nx, ny = sx + sy, sy
        if tx >= nx: yield nx, ny

    def prev_points(self, sx: int, sy: int, tx: int, ty: int) -> (int, int):
        px, py = tx, ty - tx
        if py >= sy: yield px, py
        px, py = tx - ty, ty
        if px >= sx: yield px, py
        
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        bfsq_s = deque([(sx, sy)])
        seen_s = set([(sx, sy)])
        bfsq_t = deque([(tx, ty)])
        seen_t = set([(tx, ty)])
        
        while len(bfsq_s) > 0 and len(bfsq_t) > 0:
            nx, ny = bfsq_s.popleft()
            if (nx, ny) in seen_t: return True
            seen_s.add((nx, ny))
            for nx, ny in self.next_points(nx, ny, tx, ty):
                if (nx, ny) in seen_s: continue
                bfsq_s.append((nx, ny))
            nx, ny = bfsq_t.popleft()
            if (nx, ny) in seen_s: return True
            seen_t.add((nx, ny))
            for nx, ny in self.prev_points(sx, sy, nx, ny):
                if (nx, ny) in seen_t: continue
                bfsq_t.append((nx, ny))
        return False

S = Solution()
print(S.reachingPoints(1, 1, 1000000000, 1))
