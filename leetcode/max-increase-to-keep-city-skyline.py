class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans=0
        m,n=len(grid),len(grid[0])
        res=[]
        res = []
        for col in range(m):
            temp = []
            for row in range(m):
                temp.append(grid[row][col])
            res.append(temp)
        ans=0
        for i in range(m):
            for j in range(n):
                x=max(res[j])
                y=max(grid[i])
                if grid[i][j] == x or grid[i][j]==y:
                    ans+=0
                else:
                    if x>y:
                        ans+=(y-grid[i][j])
                    else:
                        ans+=(x-grid[i][j])
        return ans

                
        