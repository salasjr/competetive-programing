# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal curr
            if not node:
                return
            inorder(node.left)
            node.left = None
            curr.right = node
            curr = node
            inorder(node.right)
        dummy = TreeNode()
        curr = dummy
        inorder(root)
        return dummy.right
            
        