class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            target = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[target]:
                    target = j
            nums[i], nums[target] = nums[target], nums[i]
        return nums