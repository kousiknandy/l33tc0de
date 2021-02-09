from typing import List
import copy, queue

def find_1(grid: List[List[int]]) -> (int, int):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                return r, c
    return None, None
            
def next_grid(grid: List[List[int]]) -> List[List[int]]:
    r1, c1 = find_1(grid)
    print(r1, c1)
    if r1 == None:
        return
    grid[r1][c1] = -1
    if (r1 - 1) >= 0:
        if grid[r1-1][c1] in [0, 2]:
            grid2 = copy.deepcopy(grid)
            if grid2[r1-1][c1] == 0:
                grid2[r1-1][c1] = 1
            yield grid2
    if (r1 + 1) < len(grid):
        if grid[r1+1][c1] in [0, 2]:
            grid2 = copy.deepcopy(grid)
            if grid2[r1+1][c1] == 0:
                grid2[r1+1][c1] = 1
            yield grid2
    if (c1 - 1) >= 0:
        if grid[r1][c1-1] in [0, 2]:
            grid2 = copy.deepcopy(grid)
            if grid2[r1][c1-1] == 0:
                grid2[r1][c1-1] = 1
            yield grid2
    if (c1 + 1) < len(grid[0]):
        if grid[r1][c1+1] in [0, 2]:
            grid2 = copy.deepcopy(grid)
            if grid2[r1][c1+1] == 0:
                grid2[r1][c1+1] = 1
            yield grid2
            

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        pathz = 0
        qu = queue.SimpleQueue()
        g3 = grid
        while True:
            for g in next_grid(g3):
                if g not in qu:
                    qu.put(g)
            g3 = qu.get()
            if not g3:
                break
            
            
#print(find_1([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
#print(find_1([[0,0,0,0],[0,0,1,0],[0,0,2,-1]]))
#print(find_1([[0,0,0,0],[0,0,0,0],[1,0,2,-1]]))

S = Solution()
S.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
