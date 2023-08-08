class Solution(object):
    def mySqrt(self, x):
        
        left = 0
        right = x
        while right>=left:
            mid = (left + right)//2

            if mid*mid<=x:
                left = mid+1
            else:
                right = mid-1       
        return right
                

                

                

                

       
       