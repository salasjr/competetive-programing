class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = Counter(s)
        tt= Counter(t)
        ans = ""
        m = tt-ss
        for a,b in m.items():
            ans+=a
        return ans
            
        
      
    
      
     
        