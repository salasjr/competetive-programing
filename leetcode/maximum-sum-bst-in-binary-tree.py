# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def valid(root):
            if not root:
                return True, 0, float("inf"), -float("inf")

            isvalidl, leftsum, lmin, lmax = valid(root.left)
            isvalidr, rightsum, rmin, rmax = valid(root.right)

            if isvalidl and isvalidr and lmax < root.val < rmin:
                curr = root.val + leftsum + rightsum
                self.max_sum = max(curr, self.max_sum)
                return True, curr, min(lmin, root.val), max(rmax, root.val)

            return False, 0, 0, 0

        self.max_sum = 0 
        valid(root)
        return self.max_sum

            
       
        
        