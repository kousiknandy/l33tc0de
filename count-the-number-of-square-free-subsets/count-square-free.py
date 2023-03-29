class Solution:
    squarefree = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
    xclusions = {
        2: [6, 10, 14, 22, 26, 30],
        3: [6, 15, 21, 30],
        5: [10, 15, 30],
        6: [10, 14, 15, 21, 22, 26, 30],
        7: [14, 21],
        10: [14, 15, 22, 26, 30],
        11: [22],
        13: [26],
        14: [21, 22, 26, 30],
        15: [21, 30],
        17: [],
        19: [],
        21: [30],
        22: [26, 30],
        23: [],
        26: [30],
        29: [],
        30: [],
    }
    freqtable = {}
    def combinations(self, nums):
        print(nums)
        if len(nums) == 0: return 0
        n = nums[0]
        if len(nums) == 1:
            return self.freqtable[n]
        wonums = nums[1:]
        winums = [x for x in nums[1:] if x not in self.xclusions[n]]
        return self.combinations(wonums) + self.freqtable[n] * (1 + self.combinations(winums))
    
    def squareFreeSubsets(self, nums: List[int]) -> int:
        self.freqtable = {}
        for n in nums:
            if n in self.squarefree:
                if n not in self.freqtable: self.freqtable[n] = 0
                self.freqtable[n] += 1
        nums = sorted([x for x in self.freqtable if x != 1])
        one = self.freqtable.get(1, 0)
        if len(nums) >= 1:
            return ((2**one) * self.combinations(nums) + (2**one - 1)) % 1000000007
        else:
            return (2**one - 1) % 1000000007
