# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        maximum=max(nums)
        idx=nums.index(maximum)
        newNode=TreeNode(maximum)
        newNode.left=self.constructMaximumBinaryTree(nums[:idx])
        newNode.right=self.constructMaximumBinaryTree(nums[idx+1:])
        return newNode






        
        