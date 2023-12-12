class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            nextnum=0
            while n>0:
                digits = n%10
                nextnum+=digits**2
                n//=10
            return nextnum
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = helper(n)
        return n==1
        
        
        
        
        