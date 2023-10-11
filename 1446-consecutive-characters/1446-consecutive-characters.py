class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)==1:
            return 1
        ans=0
        k=1
        for i in range(len(s)-1):
            if s[i] ==s[i+1]:
                k+=1
            else:
                ans=max(k,ans)
                k=1
        ans=max(ans,k)
        return ans