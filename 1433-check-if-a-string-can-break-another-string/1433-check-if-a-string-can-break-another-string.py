class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a="abcdefghijklmnopqrstuvwxyz"
        d={}
        for i in range(len(a)):
            d[a[i]]=i
        s11=[a for a in s1]
        s22=[b for b in s2]
        s11.sort()
        s22.sort()
    
        ans=set()
        for i in range(len(s11)):
            if d[s11[i]]>d[s22[i]]:
                ans.add("A")
            elif d[s11[i]]<d[s22[i]]:
                ans.add("B")
            else: 
                ans.add("C")
        if "A" in ans and "B" in ans:
            return False
        return True
        
        
    
        