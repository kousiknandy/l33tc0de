from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        r = len(triangle)
        for i in range(r-2, -1, -1):
            print(i)
            print(" ", triangle[i+1], triangle[i])
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i][j] + triangle[i+1][j],
                                     triangle[i][j] + triangle[i+1][j+1])
        return triangle[0][0]


S = Solution()
print(S.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))

