class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked={}
        for i in range(len(nums)):
            if nums[i] in checked and abs(i-checked[nums[i]])<=k:
                return True
            checked[nums[i]]=i
        return False
       
            
            
                
           
                    
       
        