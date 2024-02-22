class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mult(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=mult(x,n//2)
            res=res*res
            return x*res if n%2 else res
        res=mult(x,abs(n))
        return res if n>=0 else 1/res
            
        