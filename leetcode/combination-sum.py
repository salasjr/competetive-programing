class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path = []
        def backtrack(i):
            if sum(path)>=target:
                if sum(path)==target:
                    res.append(path[:])
                return 
            for j in range(i,len(candidates)):
                path.append(candidates[j])
                backtrack(j)
                path.pop()
        backtrack(0)
        return res
        