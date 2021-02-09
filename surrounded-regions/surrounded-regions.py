from typing import List

class Solution:
    def nextcell(self, board: List[List[str]], start) -> (int, int):
        nrows = len(board)
        ncols = len(board[0])
        i, j  = start
        if i - 1 >= 0 and board[i-1][j] == "O": yield (i-1, j)
        if i + 1 < nrows and board[i+1][j] == "O": yield (i+1, j)
        if j - 1 >= 0 and board[i][j-1] == "O": yield (i, j-1)
        if j + 1 < ncols and board[i][j+1] == "O": yield (i, j+1)
        
    def dfs(self, board: List[List[str]], start) -> None:
        dfsq  = []
        dfsq.append(start)
        while len(dfsq) > 0:
            cur = dfsq.pop(0)
            if board[cur[0]][cur[1]] == "Z":
                continue
            #print(len(dfsq), cur, board[cur[0]][cur[1]])
            board[cur[0]][cur[1]] = "Z"
            for neighbour in self.nextcell(board, cur):
                dfsq.append(neighbour)
        #self.prettyprint(board)
                
    def solve(self, board: List[List[str]]) -> None:
        nrows = len(board)
        if nrows == 0: return
        ncols = len(board[0])
        for j in range(ncols):
            if board[0][j] in ["O", "Z"]:
                self.dfs(board, (0,j))
            if board[nrows-1][j] in ["O", "Z"]:
                self.dfs(board, (nrows-1,j))
        for i in range(nrows):
            if board[i][0] in ["O", "Z"]:
                self.dfs(board, (i,0))
            if board[i][ncols-1] in ["O", "Z"]:
                self.dfs(board, (i,ncols-1))
        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Z":
                    board[i][j] = "O"

    def prettyprint(self, board: List[List[str]]) -> None:
        nrows = len(board)
        for i in range(nrows):
            print(board[i])
        print()

S = Solution()

B = [["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "O", "O", "X"],
     ["X", "X", "X", "X"],
     ["X", "O", "X", "X"],
     ["X", "X", "X", "X"]]
S.solve(B)
S.prettyprint(B)

B = [["X", "X", "X", "X"],
     ["X", "X", "O", "X"],
     ["X", "O", "O", "X"],
     ["X", "X", "X", "X"],
     ["X", "O", "X", "X"],
     ["X", "X", "X", "X"]]
S.solve(B)
S.prettyprint(B)

B = [["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "X", "X"],
     ["X", "O", "X", "X"],
     ["X", "O", "X", "X"]]
S.solve(B)
S.prettyprint(B)

B = [["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"]]
S.solve(B)
S.prettyprint(B)

B = [["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["O", "O", "O", "O"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "X", "O", "X"]]
S.solve(B)
S.prettyprint(B)

B = [["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],
     ["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],
     ["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],
     ["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],
     ["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],
     ["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],
     ["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],
     ["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],
     ["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],
     ["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],
     ["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],
     ["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],
     ["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],
     ["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],
     ["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],
     ["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],
     ["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],
     ["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],
     ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],
     ["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
S.solve(B)
S.prettyprint(B)
