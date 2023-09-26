class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        check='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        a=[]
        for i in s:
            a.append(i)   
        l=0
        r=len(s)-1
        while l < r:
            if a[l] not in check:
                l+=1
            if a[r] not in check:
                r-=1
            if a[l] in check and a[r]  in check:
                x=a[l]
                y=a[r]
                a[r] =x
                a[l]=y
                l+=1
                r-=1
        return ''.join(a)        
                
                
        