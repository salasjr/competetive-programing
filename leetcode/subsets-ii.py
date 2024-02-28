class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        path=[]
        def backtrack(i,path):
            res.append(path[:])
            if len(path)==len(nums):
                return 
            for j in range(i,len(nums)):
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()
        backtrack(0,[])
        res1=[]
        for i in res:
            if i not in res1:
                i.sort()
                res1.append(i)
        ans=[]
        for i in res1:
            if i not in ans:
                ans.append(i)
        return (ans)
        