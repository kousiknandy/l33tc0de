class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        h,t = 0,0
        z = 1 if nums[h] == 0 else 0
        w = 0
        while h < len(nums):
            print(">",w,t,h,z)
            while nums[h] == 1: 
                h += 1
                if h >= len(nums): 
                    w = max(w, h-t)
                    return w
            w = max(w,h-t)
            if z == k:
                while nums[t] == 1: t += 1
                while nums[t] == 0 and nums[h] == "0":
                    t += 1
                    h += 1
                    if h >= len(nums): return w
            print(">>",w,t,h,z)
            if nums[t] == 0:
                t += 1
                z -= 1
                # if z == 0 or t == h: break
            while nums[h] == 0 and z < k:
                h += 1
                z += 1
                if h >= len(nums):
                    w = max(w, h-t)
                    break
            w = max(w, h-t)
        return w
            
