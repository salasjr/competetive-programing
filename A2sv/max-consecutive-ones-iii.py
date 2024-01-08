class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        max_ones = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                max_ones += 1

            if (right - left + 1 - max_ones) > k:
                if nums[left] == 1:
                    max_ones -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length