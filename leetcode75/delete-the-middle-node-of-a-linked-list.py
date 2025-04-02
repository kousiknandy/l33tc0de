# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow, slower = head, head, None
        skip = False
        while True:
            fast = fast.next
            if fast is None: break
            if not skip:
                slower = slow
                slow = slow.next
            skip = not skip
        if not slower:
            head = slow.next
        else:
            slower.next = slow.next
        return head 
