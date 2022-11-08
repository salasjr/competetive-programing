class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l={}
        
        for i, j in enumerate(nums):
            r = target-j
            if r in l: return [l[r],i]
            l[j]=i
            
      