# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,count):
            if not node:
                return False
            count+=node.val;
            if not node.right and not node.left and count == targetSum:
                return True
            return (dfs(node.left,count) or dfs(node.right,count))
        
        return dfs(root,0)
        
       
        