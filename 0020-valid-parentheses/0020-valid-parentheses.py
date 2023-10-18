class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        helper={"}":"{","]":"[",")":"("}
        for i in s:
            if i in helper:
                if stack and (stack[-1] == helper[i]):
                    stack.pop()
                else:
                    return False  
            else:
                stack.append(i)
        if not stack:
            return True
        return False
        
        
       