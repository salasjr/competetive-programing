# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res=[]
        def helper(node):
            if not node:
                return 
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        def sortedArrayToBST(nums: List[int]):
            if not nums:
                return
            idx=len(nums)//2
            newNode=TreeNode(nums[len(nums)//2])
            newNode.left=sortedArrayToBST(nums[:idx])
            newNode.right=sortedArrayToBST(nums[idx+1:])
            return newNode
        return sortedArrayToBST(res)