# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        finaList = None
        lastNode = None
        k = len(lists)
        currPtrs = lists
        while True:
            maxIdx = -1
            maxVal = 0
            for i in xrange(k):
                try:
                    value = currPtrs[i]
                    if value.val > maxVal:
                        maxIdx = i
                except:
                    pass
            if maxIdx == -1:
                break
            if lastNode:
                lastNode.next = currPtrs[maxIdx]
                lastNode = lastNode.next
            else:
                lastNode = currPtrs[maxIdx]
                finaList = lastNode
            currPtrs[maxIdx] = currPtrs[maxIdx].next
        return finaList
    
