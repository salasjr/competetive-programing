class Solution:
    def reverseWords(self, s: str) -> str:
        ss=s.split()
        ans=ss[::-1]
        return " ".join(ans)
        