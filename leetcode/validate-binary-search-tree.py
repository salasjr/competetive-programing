# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev=-float("inf")
        def helper(node):
            if not node:
                return True
            if not helper(node.left):
                return False
            if node.val<=self.prev:
                return False
            self.prev=node.val 
            if not helper(node.right):
                return False
            return True
        return (helper(root))


            

        