class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i ,j = 0,len(nums)-1
        value = 0
        while value <=j:
            if nums[value] == 0:
                nums[value], nums[i] = nums[i], nums[value]
                i += 1
                value += 1
            elif nums[value] == 2:
                nums[value], nums[j] = nums[j], nums[value]
                j -= 1
            else:
                value += 1



               
                
            
       
                
            
                
                
                
        
            
       