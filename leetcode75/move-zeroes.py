class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rp, wp, l = 0, 0, len(nums)
        while rp < l:
            if nums[rp] == 0:
                rp += 1
                continue
            nums[wp] = nums[rp]
            rp += 1
            wp += 1
        while wp < l:
            nums[wp] = 0
            wp += 1
        return
