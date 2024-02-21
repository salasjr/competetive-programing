class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        j = len(nums) - 2
        
        while j >= 0:
            if nums[j] + j >= last:
                last = j
            j -= 1
        
        return last == 0

       
            
             
       
        