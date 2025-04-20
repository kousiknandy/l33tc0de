class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def nextcomb(n, k, curr, nex):
            if len(curr) == k - 1 and sum(curr) + nex == n:
                yield (*curr, nex)
                return
            if sum(curr) + nex > n or len(curr) >= k:
                return
            if nex >= 9:
                return
            yield from nextcomb(n, k, curr, nex + 1)
            yield from nextcomb(n, k, (*curr, nex), nex + 1)

        return list(nextcomb(n, k, (), 1))
