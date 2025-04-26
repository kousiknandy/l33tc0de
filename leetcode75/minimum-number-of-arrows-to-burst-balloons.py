class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        points = sorted(points, key=lambda x: x[0])
        s = points[0][0]
        e = points[0][1]
        arrows = 1
        for i in range(1, len(points)):
            s1, e1 = points[i]
            if s1 <= e: 
                e = min(e, e1)
                continue
            s, e = s1, e1
            arrows += 1
        return arrows
