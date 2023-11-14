class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        firstsum=0
        secondsum=0
        for i in range(len(nums)):
            secondsum=0
            for j in range(i+1,len(nums)):
                secondsum+=nums[j]
            if secondsum==firstsum:
                return i
            firstsum+=nums[i]
        return -1
            
                
        
    
                