from typing import List
from collections import deque

class Solution:
    def next_move(self, board, current, target, visited):
        if len(target) == 0: return
        rows = len(board)
        cols = len(board[0])
        target = target[0]
        if current[0] - 1 >= 0 and (current[0]-1, current[1]) not in visited and board[current[0]-1][current[1]] == target:
            yield (current[0]-1, current[1])
        if current[0] + 1 < rows and (current[0]+1, current[1]) not in visited and board[current[0]+1][current[1]] == target:
            yield (current[0]+1, current[1])
        if current[1] - 1 >= 0 and (current[0], current[1]-1) not in visited and board[current[0]][current[1]-1] == target:
            yield (current[0], current[1]-1)
        if current[1] + 1 < cols and (current[0], current[1]+1) not in visited and board[current[0]][current[1]+1] == target:
            yield (current[0], current[1]+1)
        
    def dfsearch(self, board, current, word, visited):
        for mv in self.next_move(board, current, word, visited):
            #print(visited, word[0], mv)
            if len(word) == 1: return True
            if self.dfsearch(board, mv, word[1:], visited + [mv]):
                return True
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for rs in range(len(board)):
            for cs in range(len(board[rs])):
                if board[rs][cs] == word[0]:
                    if self.dfsearch(board, (rs,cs), word[1:], [(rs,cs)]):
                        return True
        return False

S = Solution()
print(S.exist([["A","B","C","E"],
               ["S","F","C","S"],
               ["A","D","E","E"]],"ABCB"))
print(S.exist([["A","B","C","E"],
               ["S","F","E","S"],
               ["A","D","E","E"]], "ABCESEEEFS"))
