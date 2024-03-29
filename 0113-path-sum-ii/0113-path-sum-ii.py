# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []

        def dfs(node, path, totalcount):
            if not node:
                return

            totalcount += node.val
            temp = path + [node.val]

            if not node.left and not node.right and totalcount == targetSum:
                self.ans.append(temp)

            dfs(node.left, temp, totalcount)
            dfs(node.right, temp, totalcount)

        if not root:
            return []
        
        dfs(root, [], 0)
        return self.ans
