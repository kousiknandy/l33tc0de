class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r, w, z = 0, 0, 0, 0
        # z = 1 if nums[r] == 0 else 0
        while r < len(nums):
            if nums[r] == 0:
                if z == 0:
                    r += 1
                    z += 1
                else:
                    if nums[l] == 0: 
                        z -= 1
                    l += 1
            else:
                r += 1
            # print(w,l,r,z)
            w = max(w,r-l-z)
        return w + z - 1
