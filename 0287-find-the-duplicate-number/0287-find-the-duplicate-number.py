class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = Counter(nums)
        for key, value in s.items():
            if value >= 2:
                return key
             
