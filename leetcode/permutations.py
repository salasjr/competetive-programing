class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(i,path):
            if len(path)==len(nums):
                return 
            for j in range(len(nums)):
                path.append(nums[j])
                if len(path)==len(nums):
                    res.append(path[:])
                backtrack(j+1,path)
                path.pop()
        backtrack(0,[])
        res1=[]
        for i in res:
            if len(Counter(i))==len(nums):
                res1.append(i)
        return res1
        