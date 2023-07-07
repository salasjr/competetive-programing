class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq=int(sqrt(c))
        for i in range(sq+1):
            b = sqrt(c-(i**2))
            if b == int(b): return True
        return False
        
            
            
        
        