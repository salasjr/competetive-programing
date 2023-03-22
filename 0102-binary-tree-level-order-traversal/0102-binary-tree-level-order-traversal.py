# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
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
        return result
                
                
                    
                    
                
            
#         while(len(q)>0):
#             size = 0
#             q.popleft()
#             levelOrder(self.right, self.val)
#             levelOrder(self.left, self.val)
            
#         q = deque()
#         q.append(root.val)
#         if root is None:
#             pass
#         while(len(q)>0):
#             q.popleft()
#             levelOrder(self, root)
#             levelOrder(self.left, self.val)
#             levelOrder(self.right, self.val)   
#         return q   

    
    
    

        
        
        