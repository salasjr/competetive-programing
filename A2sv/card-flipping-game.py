class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans=set(fronts+backs)
        for i in range(len(fronts)):
            if fronts[i]==backs[i] and fronts[i] in ans:
                ans.remove(fronts[i])
        if len(ans)==0:
            return 0
        return min(ans)
      
            
            
            
           
       
            
        