class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        ans=[]
        last=d[s[0]]
        first=-1
        for i in range(len(s)):
            if i==last:
                ans.append(last-first)
                first=last
                if i<(len(s)-1):
                    last=d[s[i+1]]
            else:
                last=max(last,d[s[i]])   
        return (ans)



        
       