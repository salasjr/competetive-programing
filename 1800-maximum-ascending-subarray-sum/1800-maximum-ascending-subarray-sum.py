class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ=0
        count=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=nums[i]
            else:
                summ=max(count,summ)
                count=nums[i]
        summ=max(count,summ)
        return summ
                
                       
            
        