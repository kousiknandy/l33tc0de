class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(lambda a,b: a^b, nums, 0)
        y = 2 ** (x.bit_length() - 1)
        bins = [0, 0]
        for n in nums:
            bins[1 if n & y else 0] ^= n 
        return bins
