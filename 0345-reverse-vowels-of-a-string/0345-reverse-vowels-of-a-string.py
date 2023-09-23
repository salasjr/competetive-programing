class Solution:
    def reverseVowels(self, s: str) -> str:
        vow='aeiouAEIOU'
        l=0
        r=len(s)-1
        m=[]
        for i in range(len(s)):
            m.append(s[i])
        while l < r:
            if m[l] not in vow:
                l+=1
                
            if m[r] not in vow:
                r-=1
            if m[l] in vow and m[r] in vow:
                x,y = m[l],m[r]
                m[l] ,m[r] = y,x
                l+=1
                r-=1
        return ''.join(m)
            
     
        