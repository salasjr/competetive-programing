class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        s11=s1.split()
        s22=s2.split()
        for i in s11:
            if i not in s22:
                ans.append(i)
        for j in s22:
            if j not in s11:
                ans.append(j)
        ans1=Counter(ans)
        ans2=[]
        for a,b in ans1.items():
            if b==1:
                ans2.append(a)
        return ans2
        
        