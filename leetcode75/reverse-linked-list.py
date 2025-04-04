# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        b = head
        if not b: return head
        f = b.next
        if not f: return head
        b.next = None
        while True:
            m = f.next
            f.next = b
            if not m:
                head = f
                return head
            b = f
            f = m

