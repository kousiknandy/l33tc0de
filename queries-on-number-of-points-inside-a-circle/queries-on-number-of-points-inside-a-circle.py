import math

class Solution:
    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            x1, y1, r = q[0], q[1], q[2] 
            for p in points:
                x2, y2 = p[0], p[1]
                if self.distance(x1,y1,x2,y2) < (r + 0.0000001):
                    res[i] += 1
        return res
