from functools import partial

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lw, rw = 0, len(height)-1
        volume = lambda l, r, height: min(height[l], height[r]) * (r-l)
        water = partial(volume, height=height)
        container = water(lw,rw)
        while lw<rw:
            if height[lw] > height[rw]: rw -= 1
            else: lw += 1
            container = max(container, water(lw,rw))
        return container
