class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(x * -1)[::-1]) * -1
        
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        
        if ans > ma or ans < mi:
            return 0
        return ans
        #sum = 0
        #sign = 1
        #if x<0:
         #   sign = -1
          #  x= x*-1
        #while x>0:
         #   rem = x%10
          #  sum = sum*10 + rem
           # x=x//10
        #if not -2**31<x<2**31-1:
         #   return 0
        #return sign*sum   
         
        