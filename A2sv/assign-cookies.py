class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        l,r=0,0
        count=0
        while l<len(g) and r <len(s):
            if g[l]<=s[r]:
                count+=1
                l+=1
                r+=1
            elif g[l]>s[r]:
                r+=1
            else:
                l+=1
        return count

            