class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        count=s.count('1',1)
        if s[0]=='0':
             count+=1
        ans=count
        for c in s[1:n-1]:
            if c=='0': 
                count+=1
            else: 
                count-=1
            ans=max(ans, count)
        return ans
        
        

        