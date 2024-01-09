class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        ss1=Counter(s1)
        l=0
        r=m
        while r <= len(s2):
            ss2=Counter(s2[l:r])
            if ss2==ss1:
                return True
            l+=1
            r+=1
        return False
        