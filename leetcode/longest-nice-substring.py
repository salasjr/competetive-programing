class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(s):
            for i in range(len(s)):
                if s[i].swapcase() not in s:
                    res1=helper(s[:i])
                    res2=helper(s[i+1:])
                    return res1 if len(res1)>=len(res2) else res2
            return s
        return helper(s)




        