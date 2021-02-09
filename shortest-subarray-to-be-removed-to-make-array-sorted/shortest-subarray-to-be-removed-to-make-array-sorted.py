from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 1
        if right < 1: return 0
        for left in range(1, len(arr)):
            if arr[left] < arr[left-1]:
                left -= 1
                break
        for right in range(len(arr)-1, 0, -1):
            if arr[right] < arr[right-1]:
                break
        print(left, arr[left], ",", right, arr[right])
        while arr[left] > arr[right]:
            if left == 0:
                left -= 1
                break
            if right == len(arr) - 1:
                right += 1
                break
            if arr[left]-arr[left-1] > arr[right+1]-arr[right]:
                left -= 1
            else:
                right += 1
        print(left, ",", right)
        return max(0, right - left - 1)


S = Solution()
# print(S.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) #3
# print(S.findLengthOfShortestSubarray([2, 1, 4]))          #1
# print(S.findLengthOfShortestSubarray([5,4,3,2,1]))        #4
# print(S.findLengthOfShortestSubarray([1,2,3]))            #0
# print(S.findLengthOfShortestSubarray([2,2,2,1,1,1]))      #3
print(S.findLengthOfShortestSubarray([6,10,21,37,34,17,23,18,14,6,26,26,28,40,26,20,33,29,4,17]))
