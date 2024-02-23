# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(x,y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val !=y.val:
                return False
            return helper(x.left,y.right) and helper(x.right,y.left)
        return helper(root.left,root.right)

        
        
