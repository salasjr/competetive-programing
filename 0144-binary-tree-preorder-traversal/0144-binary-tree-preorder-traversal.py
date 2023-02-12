# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        m=[]
        stack=[root]
        while stack:
            x=stack.pop()
            if x:
                m.append(x.val)
                stack.append(x.right)
                stack.append(x.left)
        return m
  
        