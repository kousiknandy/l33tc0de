# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def next_turn(self):
        yield from itertools.cycle([(0,1),(1,0),(0,-1),(-1,0)])

    def gen_spiral(self, row, col):
        gd = self.next_turn()
        yield from itertools.repeat(next(gd), col-1)
        for i in range(min(row,col)):
            yield from itertools.repeat(next(gd), row-i-1)
            yield from itertools.repeat(next(gd), col-i-1)

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for c in range(n)] for r in range(m)]
        r, c = 0, 0
        k = head
        res[r][c] = k.val
        for i, j in self.gen_spiral(m, n):
            r += i
            c += j
            k = k.next
            if k:
                res[r][c] = k.val
            else:
                break
        return res
