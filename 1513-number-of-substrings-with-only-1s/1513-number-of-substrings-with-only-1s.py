class Solution:
    def numSub(self, s: str) -> int:
        ans=0
        count=0
        r=0
        mod=10**9 + 7.
        while r<len(s):
            if s[r]=="1":
                count+=1 
            else:
                ans+=(count*(count+1)//2)%mod
                count=0
            r+=1
        ans+=(count*(count+1)//2)%mod
        return int(ans)
      
        
        
        