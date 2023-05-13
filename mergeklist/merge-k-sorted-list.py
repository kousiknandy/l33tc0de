# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getnext(self, list, idx):
        l = list
        while l:
            yield (l.val, idx)
            l = l.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        lists = filter(None, lists)
        gl = [self.getnext(l,i) for i,l in enumerate(lists)]
        el = [next(l) for l in gl]
        res = tail = None
        heapq.heapify(el)
        while len(el):
            v, i = heapq.heappop(el)
            n = ListNode(v)
            if not res: res = n
            if tail: tail.next = n
            tail = n
            try:
                v, i = next(gl[i]) # replenish
                heapq.heappush(el, (v, i))
            except StopIteration:
                pass
        return res        
