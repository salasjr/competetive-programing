class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fun2(x,n):
            if x ==0: return 0
            if n==0: return 1
            res = fun2(x,n//2)
            res = res*res
            return x*res if n%2 else res
        res=fun2(x,abs(n))
        if n>=0:
            return res
        return 1/res
        