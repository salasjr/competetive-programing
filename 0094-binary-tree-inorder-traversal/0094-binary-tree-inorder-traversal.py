# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        m=[]
        def checkk(Node):
            if not Node:
                return Node
            checkk(Node.left)
            m.append(Node.val)
            checkk(Node.right)
        checkk(root)
        return  m
            
       