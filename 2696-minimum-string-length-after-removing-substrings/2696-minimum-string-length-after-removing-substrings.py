class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>1:
                if "".join(stack[-2:]) in ["AB","CD"]:
                    stack.pop()
                    stack.pop()
                    
        return len(stack)
                
        