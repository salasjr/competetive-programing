# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def helper(root):
            if not root:
                return None
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        ans1=Counter(ans)
        mydict = dict(sorted(ans1.items(), key=lambda item: item[1],reverse=True))
        max_value = max(mydict.values())
        ans2=[]
        for a,b in mydict.items():
            if b!=max_value:
                break
            else:
                ans2.append(a)
        return ans2
      
       
