class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        def search(arr, l, r, target, cache):
            if target in cache:
                return cache[target]
            n = r - l + 1
            if arr[l] >= target:
                cache[target] = n
                return n
            if arr[r] < target:
                cache[target] = 0
                return 0
            while l < r:
                m = (l + r) // 2
                # print(arr,l,m,r,target)
                if arr[m] == target:
                    while m > 0 and arr[m - 1] == target:
                        m -= 1
                    cache[target] = n - m
                    return n - m
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            v = n - l if arr[l] >= target else n - l - 1
            cache[target] = v
            return v

        potions.sort()
        cache = {}
        return [
            search(
                potions,
                0,
                len(potions) - 1,
                divmod(success, x)[0] + (1 if divmod(success, x)[1] else 0),
                cache,
            )
            for x in spells
        ]
