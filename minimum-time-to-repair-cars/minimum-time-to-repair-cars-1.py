import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def completes(t: int, ranks: List[int], cars: int) -> bool:
            cc = [math.isqrt(t//r) for r in ranks]
            return sum(cc) >= cars

        ll, m, ul = 1, 1, 1
        while True:
            if completes(ul, ranks, cars): break
            ll, m, ul = ul, ul, ul*2
        while ll < ul:
            m = (ll+ul)//2
            if completes(m, ranks, cars): ul = m
            else: ll = m + 1
        return m if completes(m, ranks, cars) else m+1
        
