class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=[i for i in s]
        ss="QWERTYUIOPASDFGHJKLZXCVBNM"
        for j in range(len(ans)):
            if ans[j] in ss:
                ans[j]=ans[j].lower()
        return "".join(ans)
        