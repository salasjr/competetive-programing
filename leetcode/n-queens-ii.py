class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        dig1=set()
        dig2=set()

        grid=[["."]*n for _ in range(n)]
        res=0
        def backtrack(r):
            nonlocal res
            if r==n:
                res+=1
                return
            for c in range(n):
                if c in col or (c+r) in dig1 or (r-c) in dig2:
                    continue
                col.add(c)
                dig1.add(c+r)
                dig2.add(r-c)
                backtrack(r+1)
                col.remove(c)
                dig1.remove(c+r)
                dig2.remove(r-c)
        backtrack(0)
        return res
        