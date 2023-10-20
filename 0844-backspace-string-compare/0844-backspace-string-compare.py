class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stack1=[]
        for i in s:
            if stack and i =="#":
                stack.pop()
            else:
                stack.append(i)
        for j in t:
            if stack1 and j=="#":
                stack1.pop()
            else:
                stack1.append(j)
        st1 = [item for item in stack if item != '#']
        st2 = [item for item in stack1 if item != '#']
        return st1==st2
                
            
        
        