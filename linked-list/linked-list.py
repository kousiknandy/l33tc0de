class Link:
    __slots__ = ["val", "next", "__weakref__"]
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.sz = 0

    def __repr__(self):
        s = "(" + str(self.sz) + ") "
        cur = self.head
        while cur:
            s += str(cur.val) + "->"
            cur = cur.next
        return s

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.sz - 1:
            return -1
        if index == self.sz - 1:
            return self.tail.val
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Link()
        node.val = val
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.sz += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Link()
        node.val = val
        node.next = None
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.sz += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.sz:
            return
        if index == self.sz:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        prev = None
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        node = Link()
        node.val = val
        node.next = cur
        prev.next = node
        self.sz += 1
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.sz - 1:
            return
        cur = self.head
        prev = None
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next
        if cur == self.tail:
            self.tail = prev
        self.sz -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

L = MyLinkedList()
L.addAtHead(2)
print(L)
L.addAtHead(1)
print(L)
L.addAtTail(6)
print(L)
L.addAtIndex(2, 4)
print(L)
L.addAtIndex(2, 3)
print(L)
L.deleteAtIndex(1)
print(L)
L.deleteAtIndex(3)
print(L)
L.addAtTail(5)
print(L)

L = MyLinkedList()
L.addAtTail(10)
print(L)
L.addAtTail(5)
print(L)
print()

L = MyLinkedList()
L.addAtHead(7)
print(L)
L.addAtHead(2)
print(L)
L.addAtHead(1)
print(L)
L.addAtIndex(3,0)
print(L)
L.deleteAtIndex(2)
print(L)
L.addAtHead(6)
print(L)
L.addAtTail(4)
print(L)
L.get(4) #4
print(L)
L.addAtHead(4)
print(L)
L.addAtIndex(5,0)
print(L)
L.addAtHead(6)
print(L)
print()
#[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

L = MyLinkedList()
L.addAtHead(1)
print(L)
L.addAtTail(3)
print(L)
L.addAtIndex(1,2)
print(L)
L.get(1) #2
L.deleteAtIndex(0)
print(L)
L.get(0) #2
#[[],[1],[3],[1,2],[1],[0],[0]]
