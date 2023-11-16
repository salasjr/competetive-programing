class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == summ - nums[i]:
                return i
            left_sum += nums[i]
            summ -= nums[i]

        return -1

            
        