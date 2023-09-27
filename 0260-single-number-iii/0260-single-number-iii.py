class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        sor= dict(sorted(a.items(), key=lambda item: item[1]))
        ans = list(sor.keys())[:2]
        return ans

        