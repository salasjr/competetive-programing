# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max2(root, height):
            if not root:
                return height
            return max(max2(root.left,height+1),max2(root.right,height+1))
        return max2(root,0)
    
