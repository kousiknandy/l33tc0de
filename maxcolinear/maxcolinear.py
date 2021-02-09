from itertools import combinations

# Definition for a point.
#class Point(object):
#    def __init__(self, a=0, b=0):
#        self.a = a
#        self.b = b
#         
#    def __repr__(self):
#        return str(self.a) + "," + str(self.b)

class Solution(object):

    @classmethod
    def slope_intercept(cls, point1, point2):
        try:
            slope = 1.0 * (point1.y - point2.y)/(point1.x - point2.x)
        except ZeroDivisionError:
            slope = 9223372036854775807        
        intercept = point2.y - (point2.x * slope)
        return (slope, intercept)
        
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        segments = {}
        for p in combinations(points, 2):
            s_i = self.slope_intercept(p[0], p[1])
            #print p, s_i
            cur = segments.get(s_i, set())
            cur.add(p[0])
            cur.add(p[1])
            segments[s_i] = cur 
        mx = 0
        for k in segments.keys():
            if mx < len(segments[k]):
                mx = len(segments[k])

        return mx
    
#if __name__ == "__main__":
#    L = []
#    L.append(Point(2,3))
#    L.append(Point(4,6))
#    L.append(Point(5,6))
#    L.append(Point(10,8))
#    L.append(Point(8,12))
#    s = Solution()
#    print s.maxPoints(L)
