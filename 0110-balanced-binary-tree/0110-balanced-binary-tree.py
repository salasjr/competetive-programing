# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root: return [True,0]
            left,right = check(root.left),check(root.right)
            sucess = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [sucess, 1 + max(right[1],left[1])]
        return check(root)[0]
                                                  
                                                  
        
        
            
        