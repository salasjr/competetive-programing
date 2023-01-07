class Solution:
    def fib(self, n: int) -> int:
        def fib1(n):
            if n <= 1:
                return n
            else:
                return (fib1(n-1)+fib1(n-2))
        return fib1(n)
            
        
        
     
        