from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(distances)
        print(distances)
        return [x[1] for x in heapq.nsmallest(K, distances)]

S = Solution()
print(S.kClosest([[3,3],[5,-1],[-2,4]], 2))

