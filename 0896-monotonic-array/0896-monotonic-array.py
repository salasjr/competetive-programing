class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ans=sorted(nums)
        ans1=list(reversed(ans))
        if nums == ans or nums==ans1:
            return True
        else:
            return False
        
       
            
                
        
            
        