class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        if needle == haystack:
            return 0
        m=len(needle)
        n= len(haystack)
        for i in range(len(haystack)+1):
            for j in range(len(haystack)+1):
                m=haystack[i:j]
                if m==needle:
                    return i
        return -1
        