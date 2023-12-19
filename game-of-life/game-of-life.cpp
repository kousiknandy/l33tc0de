class Solution {
public:
    std::tuple<int, int> neighbours(vector<vector<int>>& board, int row, int col, int maxr, int maxc) {
        int live = 0, dead = 0;
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0) continue;
                int r = row + i, c = col + j;
                if (r >= 0 && r < maxr && c >= 0 && c < maxc) {
                    int v = board[r][c] & 1;
                    if (v) live++;
                    else dead++;
                }
            }
        }
        return std::make_tuple(live, dead);
    }
    void gameOfLife(vector<vector<int>>& board) {
        int maxr = board.size();
        int maxc = board[0].size();
        int live, dead;
        for (int i = 0; i < maxr; i++) {
            for (int j = 0; j < maxc; j++) {
                tie(live, dead) = neighbours(board, i, j, maxr, maxc);
                if (board[i][j] & 1) {
                    if (live == 2 or live == 3) board[i][j] |= 0x2;
                } else {
                    if (live == 3) board[i][j] |= 0x2;
                }
            }
        }
        for (int i = 0; i < maxr; i++) {
            for (int j = 0; j < maxc; j++) {
                board[i][j] >>= 1;
            }
        }
    }
};
