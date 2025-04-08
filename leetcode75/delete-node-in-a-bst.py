# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def insert_node(root, node):
            # print("insert", root.val, node.val)
            if root.val > node.val:
                if root.left: insert_node(root.left, node)
                else: root.left = node
            else:
                if root.right: insert_node(root.right, node)
                else: root.right = node

        def search_del(root, key):
            # print("search", root.val, key)
            if root.left and root.left.val == key:
                np = root.left.left or root.left.right
                if root.left.left and root.left.right: 
                    insert_node(root.left.left, root.left.right)
                root.left = np
                return
            if root.right and root.right.val == key:
                np = root.right.left or root.right.right
                if root.right.left and root.right.right: 
                    insert_node(root.right.left, root.right.right)
                root.right = np
                return
            if root.left: search_del(root.left, key)
            if root.right: search_del(root.right, key)

        if not root: return None
        if root.val == key:
            if not root.left: return root.right
            if not root.right: return root.left
            insert_node(root.left, root.right)
            return root.left
        search_del(root, key)
        return root
