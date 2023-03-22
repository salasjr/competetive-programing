# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        s=[]
        queue = [root]
        nextqueue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    nextqueue.append(root.left)
                if root.right is not None:
                    nextqueue.append(root.right)
            result.append(level)
            level =[]
            queue = nextqueue
            nextqueue =[]
        x = reversed(result)
        return x
        