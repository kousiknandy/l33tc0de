# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class LinkedList:
    def __init__(self, A):
        self.head = A

    def reverse(self, n=None):
        #import pdb; pdb.set_trace()
        curr = n if n else self.head
        next = curr.next
        curr.next = None
        while curr:
            if not next:
                break
            temp = next.next
            next.next = curr
            curr = next
            next = temp
        self.head = curr

    def __repr__(self):
        s = ">"
        curr = self.head
        while curr:
            s += str(curr.val)
            s += "->"
            curr = curr.next
        return s

    def midpt(self):
        f = s = self.head
        h = 1
        while f:
            f = f.next
            h += 1
            if h % 2:
                s = s.next
        return s if h % 2 else s.next
    
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        ll = LinkedList(A)
        lr = LinkedList(A)
        m = lr.midpt()
        if not m:
            return ll.head
        lr.reverse(m)
        el = ll.head
        er = lr.head
        print(ll, lr)
        while er:
            el.val = er.val - el.val
            el = el.next
            er = er.next
        er = LinkedList(lr.head)
        er.reverse()
        print(ll, er)
        #m.next = er.head
        return ll.head

def makelist(a):
    c = None
    h = None
    m = None
    for e in a:
        x = ListNode(e)
        if c:
            c.next = x
        c = x
        if not h:
            h = x
    l = LinkedList(h)
    return l

S = Solution()
l = makelist([3, 4, 2, 7, 8, 10])
x = S.subtract(l.head)
print(LinkedList(x))
l = makelist([3, 4, 2, 8, 10])
x = S.subtract(l.head)
print(LinkedList(x))
l = makelist([1])
x = S.subtract(l.head)
print(LinkedList(x))

# l = makelist([310])
# print(l)
# l = makelist([3, 4])
# print(l)

