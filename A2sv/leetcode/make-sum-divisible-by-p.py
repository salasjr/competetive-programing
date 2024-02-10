class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        d = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            cur = (cur + a) % p
            d[cur] = i
            if (cur - need) % p in d:
                res = min(res, i - d[(cur - need) % p])
        return res if res < n else -1
        