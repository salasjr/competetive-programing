class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        currmax=nums[0]
        summ=nums[0]
        for i in range(1,len(nums)):
            summ+=nums[i]
            currmax=max(currmax,(math.ceil(summ/(i+1))))
        return currmax

        





        