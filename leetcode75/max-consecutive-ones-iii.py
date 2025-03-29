class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        h,t,w,z = 0,0,0,0
        while True:
            # print("",w,t,nums[t],h, nums[h],z)
            if nums[h] == 1: h += 1
            w = max(w, h-t)
            if h >= len(nums): break
            if z == k and nums[h] == 0 and nums[t] == 0:
                h += 1
                t += 1
                if h >= len(nums): break
            if z < k and nums[h] == 0:
                h += 1
                z += 1
            w = max(w, h-t)
            if h >= len(nums): break
            # print(" ",w,t,nums[t],h, nums[h],z)
            if z == k:
                if nums[h] == 0:
                    if nums[t] == 0: z -= 1
                    t += 1
        return w
