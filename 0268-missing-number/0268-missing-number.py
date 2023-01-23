class Solution(object):
    def missingNumber(self, nums):
        sum1 = sum(nums)
        n=len(nums)
        sum2 = n*n + n
        sum3=sum2/2
        return sum3-sum1
        
     
        
    
            
        
        
  