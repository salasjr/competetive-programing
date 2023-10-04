class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        f=sorted(nums)
        for i in range(len(nums)):
            a.append(f.index(nums[i]))
        return a
            
        