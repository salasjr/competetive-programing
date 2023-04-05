# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def secondd(childr, childl):
            if not childr and not childl:
                return True
            if not childr or not childl:
                return False
            if childr.val != childl.val:
                return False
            return secondd(childr.right,childl.left) and secondd(childr.left,childl.right)
        return secondd(root.right,root.left)
            

       
            
       
      