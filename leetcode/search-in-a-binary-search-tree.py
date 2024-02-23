# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=[]
        def helper(node,num):
            if not node:
                return None
            if node.val>num:
                helper(node.left,num)
            elif node.val<num:
                helper(node.right,num)
            else:
                ans.append(node)
            return ans
        z=(helper(root,val))
        if z:
            return z[0]
        return None
        

        