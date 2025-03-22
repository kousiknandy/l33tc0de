class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i in range(len(nums)):
            ans += "1" if nums[i][i] == "0" else "0"
        return ans
