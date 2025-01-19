class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        i = 0
        mx = nums[i]
        mn = nums[-1]
        bump = 0
        while mx > mn:
            bump += mx - mn
            mn += mx - mn
            mx = nums[i+1] + bump
            i += 1
        return bump
