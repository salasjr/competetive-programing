class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)<3:
            return list(set(nums))
        m= Counter(nums)
        keys = [key for key, value in m.items() if value > len(nums)/3]
        return keys
        

        
      
       

            
        