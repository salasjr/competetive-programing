class Solution:
    def countHomogenous(self, s: str) -> int:
        ans=0
        count=1
        mod=10**9 + 7.
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                ans+=(count*(count+1)//2)%mod
                count=1
        ans+=(count*(count+1)//2)%mod
        return int(ans)        
      