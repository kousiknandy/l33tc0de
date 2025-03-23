class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        ans = [x+extraCandies>=mx for x in candies]
        return ans
