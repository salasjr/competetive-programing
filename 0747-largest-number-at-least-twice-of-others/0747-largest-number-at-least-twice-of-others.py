class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        b= max(nums)
        c=nums.index(b)
        nums.sort()
        if nums[-2]*2 <=nums[-1]:
            return c
        return -1
        