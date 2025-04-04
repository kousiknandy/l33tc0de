# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front, mid, tail = None, None, None
        tail = head
        if not tail: return head
        mid = head.next
        if not mid: return head
        even = mid
        front = mid.next
        if not front: return head
        odd = False
        while True:
            tail.next = front
            mid.next = None
            tail = mid
            mid = front
            odd = not odd
            front = front.next
            if not front: break
        if odd:
            mid.next = even
        else:
            tail.next = even
        return head
