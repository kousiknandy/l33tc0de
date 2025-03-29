class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        watermarks = [None, None]
        for n in nums:
            if watermarks[0] is None: 
                watermarks[0] = n
                continue
            if n <= watermarks[0]: watermarks[0] = n
            elif watermarks[1] is None or n <= watermarks[1]: watermarks[1] = n
            else: return True
        return False 
