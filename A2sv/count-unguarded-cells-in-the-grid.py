class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        guards_set = {(x, y) for x, y in guards}
        walls_set={(x,y) for x,y in walls}
        for x,y in guards:
            a,b=x,y
            while b+1<n:
                if (a,b+1) in walls_set:
                    break
                elif (a,b+1) in guards_set:
                    break
                else:
                    matrix[a][b+1]=1
                b+=1
            a,b=x,y
            while b-1>=0:
                if (a,b-1) in walls_set:
                    break
                elif (a,b-1) in guards_set:
                    break
                else:
                    matrix[a][b-1]=1
                b-=1
            a,b=x,y
            while a+1<m:
                if (a+1,b) in walls_set:
                    break
                elif (a+1,b) in guards_set:
                    break
                else:
                    matrix[a+1][b]=1
                a+=1
            a,b=x,y
            while a-1>=0:
                if (a-1,b) in walls_set:
                    break
                elif (a-1,b) in guards_set:
                    break
                else:
                    matrix[a-1][b]=1
                a-=1
        count=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    count+=1
        return count-len(guards)-len(walls)
                
        
            
        
       
                
        
      
                
           
       
        
            
            
            
                
        