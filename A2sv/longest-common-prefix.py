class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        min1 = min(strs,key=len)
        for i, ch in enumerate(min1):
            for other in strs:
                if other[i] != ch:
                    return min1[:i]
        return min1