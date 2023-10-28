class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1=Counter(s)
        s2=Counter(t)
        count=0
        m=s1-s2
        for a,b in m.items():
            count+=b
        return count
            
        