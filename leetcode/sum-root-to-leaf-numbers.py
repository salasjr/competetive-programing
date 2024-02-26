# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []     
        def helper(root, path):
            if not root:
                return           
            path = path + str(root.val)            
            if not root.left and not root.right:
                stack.append(path)
                return           
            helper(root.left, path)
            helper(root.right, path)        
        helper(root, "")        
        total_sum = sum(int(path) for path in stack)        
        return total_sum
        
     
       



        

        

        