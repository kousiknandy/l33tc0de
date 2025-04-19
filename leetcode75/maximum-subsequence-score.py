import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combo = sorted(zip(nums2,nums1), reverse=True)
        hip1 =[x[1] for x in combo[:k]]
        heapq.heapify(hip1)
        min2 = combo[k-1][0]
        max1 = sum(hip1)
        maxp = min2 * max1
        for i in range(k,len(nums2)):
            min2 = combo[i][0]
            it = heapq.heappushpop(hip1, combo[i][1])
            max1 += combo[i][1] - it
            p = min2 * max1
            # print(min2, hip1, p, maxp)
            maxp = max(maxp, p)
        return maxp
