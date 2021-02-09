class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        barriers = []
        for i in range(len(height)):
            lbarrier = 0
            rbarrier = 0
            try:
                print(height[:i])
                lbarrier = max(height[:i])
            except:
                pass
            try:
                print(height[i:])
                rbarrier = max(height[i:])
            except:
                pass
            barriers.append((lbarrier,rbarrier))
        print(barriers)
        total = 0
        for i in range(len(height)):
            total += max([min([barriers[i][0], barriers[i][1]]) - height[i], 0])
        return total

if __name__ == "__main__":
        s = Solution()
        print(s.trap([2,0,2]))
