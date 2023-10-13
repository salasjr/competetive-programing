class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1=Counter(s)
        s2=Counter(goal)
        if s1 !=s2:
            return False
        ans=[]
        for j  in range(len(s)):
            ans.append(s[j])
        print(ans)
        for i in range (len(s)):
            a=ans.pop(0)
            ans.append(a)
            if "".join(ans) == goal:
                return True
        return False
        