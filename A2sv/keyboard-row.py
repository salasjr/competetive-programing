class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a="qwertyuiopQWERTYUIOP"
        b="asdfghjklASDFGHJKL"
        c="zxcvbnmZXCVBNM"
        def checker(s,c):
            for j in s:
                if j not in c :
                    return False
            return True
        ans=[]
        for i in words:
            if checker(i,a):
                ans.append(i)
            elif checker(i,b):
                ans.append(i)
            elif checker(i,c):
                ans.append(i)
            else:
                continue
        return ans