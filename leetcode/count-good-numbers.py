class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        def mult(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=mult(x,n//2)%mod
            res=res*res
            return x*res if n%2 else res    
        if n%2:
            return (mult(5,(n//2)+1)*mult(4,n//2))%mod
        else:
            return (mult(5,n//2)*mult(4,n//2))%mod
