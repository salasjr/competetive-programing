# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def helper(node):
            if not node:
                return None
            if node:
                ans.append(node.val)
            helper(node.left)
            helper(node.right)
            return ans
        z=(helper(root))
        z.sort()
        return z[k-1]
            
            
            
        