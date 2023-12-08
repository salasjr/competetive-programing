class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        for i in range(len(s)):
            if i==spaces[-1]:
                ans+=" "
                ans+=s[i]
            elif i< spaces[-1] and i ==spaces[j]:
                ans += " "
                ans += s[i]
                j += 1
            else:
                ans += s[i]
        return ans

        
      