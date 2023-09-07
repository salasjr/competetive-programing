# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        def dfs(node):
            if not node:
                return 
            if not node.left and not node.right:
                return
            x= node.left
            y = node.right
            node.left = y
            node.right = x
            dfs(x)
            dfs(y)
            return node
        return dfs(root)
       
            
           
            
        