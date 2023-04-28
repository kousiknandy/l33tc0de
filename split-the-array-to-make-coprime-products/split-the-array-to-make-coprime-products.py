class Solution:
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,]

    def findValidSplit(self, nums: List[int]) -> int:
        dr = (len(nums), -1)
        f_table = {}

        @lru_cache
        def factors(n):
            f = []
            if n == 1: 
                return [1]
            for p in self.primes:
                if p > n: break
                if n % p: continue
                while n % p == 0:
                    n //= p
                f.append(p)
            else:
                return f + [n]
            return f

        if len(nums) <= 1: return -1
        if nums[0] == 1: return 0
        for ix, n in enumerate(nums):
            for f in factors(n):
                mn,mx = f_table.get(f, dr)
                f_table[f] = (min(ix,mn), max(mx,ix))
        # print(f_table)
        for ix, n in enumerate(nums):
            # if ix>4500: print(ix, n, [f_table[x] for x in factors(n)])
            mn = min([f_table[x][0] for x in factors(n)])
            mx = max([f_table[x][1] for x in factors(n)])
            # print(ix, n, mn, mx)
            nums[ix] = (n, mn, mx) if n != 1 else (n, ix, ix)
        li = nums[0][2]
        i = li + 1
        while i < len(nums):
            if nums[i][1] > li: 
                i += 1
                continue
            li = nums[i][2]
            if li == len(nums)-1: break
            i = li + 1
        return li if li < len(nums)-1 else -1 
