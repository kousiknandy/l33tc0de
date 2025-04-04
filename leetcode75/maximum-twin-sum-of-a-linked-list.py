# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s1 = head.next
        s2 = head
        f = head
        while True:
            f = f.next
            f = f.next
            if not f: break
            # print("f", f.val)
            m = s1.next
            if not m: break
            s1.next = s2
            if s2 == head: s2.next = None
            s2 = s1
            s1 = m
            # print("s1,s2", s1.val, s2.val)
        mx = 0
        # s2 = s1.next
        print(s1.val,s2.val)
        while s1 and s2:
            mx = max(mx, s1.val + s2.val)
            s1 = s1.next
            s2 = s2.next
        return mx
