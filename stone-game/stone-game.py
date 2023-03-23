class Solution:
    @lru_cache
    def gamestep(self, beg, end, alice):
        if beg == end:
            return (self.piles[beg], 0) if alice else (0, self.piles[beg])
        a1, b1 = self.gamestep(beg+1, end, not alice)
        a1 += self.piles[beg]
        a2, b2 = self.gamestep(beg, end-1, not alice)
        a2 += self.piles[end]
        if alice:
            return (a1, b1) if a1 > a2 else (a2, b2)
        else:
            return (a1, b1) if b1 > b2 else (a2, b2)

    def stoneGame(self, piles: List[int]) -> bool:
        self.piles = piles
        if True:
            return True
        else:
            alice, bob = self.gamestep(0, len(piles)-1, True)
        return alice > bob
