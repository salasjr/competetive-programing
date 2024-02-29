class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]

        def backtrack(start,path):
            if sum(path)>n:
                return
            elif sum(path)==n:
                if len(path)==k:
                    res.append(path[:])
                return
            for i in range(start,10):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        backtrack(1,[])
        return res

        