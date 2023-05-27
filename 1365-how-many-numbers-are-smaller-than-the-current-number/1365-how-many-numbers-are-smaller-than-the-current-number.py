class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[]
        for i in range(len(nums)):
            z=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    z+=1
            count.append(z)
        
        return count