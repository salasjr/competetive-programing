class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        dig1=set()
        dig2=set()

        grid=[["."]*n for _ in range(n)]
        res=[]
        def backtrack(r):
            if r==n:
                ans=["".join(row) for row in grid]
                res.append(ans)
            
            for c in range(n):
                if c in col or (r+c) in dig1 or (r-c) in dig2:
                    continue
                col.add(c)
                dig1.add(r+c)
                dig2.add(r-c)
                grid[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                dig1.remove(r+c)
                dig2.remove(r-c)
                grid[r][c]="."
        backtrack(0)
        return res


       