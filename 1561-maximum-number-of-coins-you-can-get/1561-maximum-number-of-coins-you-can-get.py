class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        lenn=len(piles)//3
        count=0
        for i in range(lenn):
            count+=piles[i*2+1]
        return count
            

        
  
            
        
        
        
        
        