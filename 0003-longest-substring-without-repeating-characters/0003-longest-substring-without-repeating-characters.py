class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempdic = {}
        left = 0
        res = 0
        for i in range(len(s)):

            if s[i] not in tempdic:
                res = max(res,i- left +1)

            else:
                if tempdic[s[i]] < left:
                    res = max(res,i - left +1)
                else:
                    left = tempdic[s[i]] + 1
            tempdic[s[i]] = i
        return res
## this failed at 922 out of 987 test cases
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        else:
            s = [s[i] for i in range(len(s))]
            count = 0
            for i in range(1,len(s)):
                if s[i]  in s[:i]:
                    count += 1
                    break
            if count < 1:
                return len(s)      
        i=j=0
        res=[]
        while i <= j and j< len(s):
            slide = s[i:j]
            res.append(len(slide))
            if s[j] in slide:
                while s[i] != s[j]:
                    i += 1
                i += 1
            j += 1
            res.sort()
        return res[-1]