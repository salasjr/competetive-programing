class Solution:
    def minimumSteps(self, s: str) -> int:
        d={}
        count0=s.count("0")
        summ=0
        ans=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                summ+=1
            d[i]=summ
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                ans+=d[i]
        return ans
        