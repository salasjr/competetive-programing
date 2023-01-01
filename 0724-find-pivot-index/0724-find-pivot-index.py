class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums[1:])
        leftSum = 0
        for i in range(len(nums)-1):
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            rightSum -= nums[i+1] 
        if rightSum == leftSum:
            return len(nums)-1
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
      