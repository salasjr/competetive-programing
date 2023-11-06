class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        l,r=0,2
        ans=[i for i in s]
        count=0
        while r<len(s):
            a=set(ans[l:r+1])
            b=ans[l:r+1]
            if len(a)==len(b):
                count+=1
            l+=1
            r+=1
        return count
        