from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        walklen = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        walkdir = [1, 1, -1, -1]
        m = len(matrix)
        n = len(matrix[0])
        startpos = (0, -1)
        results = []
        for i in range(m+n):
            r = i % 2 == 0
            w = n - walklen[i] if r else m - walklen[i]
            print(m, n, w)
            if not w: break
            for j in range(0, w):
                if r:
                    startpos = (startpos[0], startpos[1] + walkdir[i%4])
                else:
                    startpos = (startpos[0] + walkdir[i%4], startpos[1])
                print(startpos, end=" ")
                results.append(matrix[startpos[0]][startpos[1]])
        return results

S = Solution()
print(S.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
