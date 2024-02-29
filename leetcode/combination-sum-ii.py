class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        candidates.sort()

        def backtrack(index,path,pathsum):
            if pathsum>target:
                return 
            elif pathsum==target:
                ans.add(tuple(path))
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,pathsum+path[-1])
                path.pop()
        backtrack(0,[],0)
        return ans
       