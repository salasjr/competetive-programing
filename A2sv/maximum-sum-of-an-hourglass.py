class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans=[]
        for i in range(len(grid[0])-2):
            for j in range(len(grid)-2):
                z=0
                z+=sum(grid[j][i:i+3])
                z+=sum(grid[j+2][i:i+3])
                z+=(grid[j+1][i+1])
                ans.append(z)
        return max(ans)
            
      
            
            
        

        