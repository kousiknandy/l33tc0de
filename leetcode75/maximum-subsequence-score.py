class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combo = sorted(zip(nums2,nums1), reverse=True)
        hip1 =[x[1] for x in combo[:k]]
        min2 = combo[k-1][0]
        maxp = min2 * sum(hip1)
        for i in range(k,len(nums2)):
            min2 = combo[i][0]
            hip1.append(combo[i][1])
            p = min2 * sum(heapq.nlargest(k, hip1))
            # print(min2, hip1, p, maxp)
            maxp = max(maxp, p)
        return maxp
