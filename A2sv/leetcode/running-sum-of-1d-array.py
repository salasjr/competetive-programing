class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum=[0]
        for i in range(len(nums)):
            presum.append(presum[-1]+nums[i])
        presum.pop(presum[0])
        return presum