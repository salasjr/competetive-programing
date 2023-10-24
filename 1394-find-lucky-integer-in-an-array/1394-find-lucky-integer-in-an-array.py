class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s=Counter(arr)
        sorted_s = sorted(s.items(), key=lambda x: x[1], reverse=True)
        for a,b in sorted_s:
            if a==b:
                return a
        return -1