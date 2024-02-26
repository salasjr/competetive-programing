class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        def backtrack(i,path):
            if len(path)==len(nums):
                return 
            for j in range(i,len(nums)):
                path.append(nums[j])
                res.append(path[:])
                backtrack(j+1,path)
                path.pop()
        backtrack(0,[])
        return res
       