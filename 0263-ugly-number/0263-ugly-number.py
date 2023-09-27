class Solution:
    def isUgly(self, n: int) -> bool:
        if n <=0:
            return False
        a=set()
        while n>1:
            if n%2 ==0:
                z=n%2
                a.add(z)
                n =n//2
            elif n%3==0:
                z=n%2
                a.add(z)
                n=n//3
            elif n%5==0:
                z=n%2
                a.add(z)
                n=n//5
            else:
                a.add(0)
                return False
        return True
            
       
        
        