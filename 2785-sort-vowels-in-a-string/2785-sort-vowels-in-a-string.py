class Solution:
    def sortVowels(self, s: str) -> str:
        voewel = 'AEIOUaeiou'
        ans=[]
        ans1=[]
        for i in s:
            if i in voewel:
                ans.append(1)
                ans1.append(i)
            else:
                ans.append(i)
        ans1.sort()
        for i in range(len(ans)):
            if ans[i]==1:
                ans[i]=ans1[0]
                ans1.pop(0)
        return "".join(ans)
        
        