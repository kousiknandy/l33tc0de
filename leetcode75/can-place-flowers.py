class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        if n == 0: return True
        if not flowerbed: return False
        c = flowerbed[0]
        k = 0
        for c,k in itertools.pairwise(flowerbed):
            if p or c or k:
                p = c
                continue
            p = 1
            c = 1
            n -= 1
            if n == 0: return True
        if n == 1 and c == 0 and k == 0: return True
        return False
