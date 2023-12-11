class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans=Counter(arr)
        ans1 = dict(sorted(ans.items(), key=lambda item: item[1],reverse=True))
        for a in ans1:
            return a
        