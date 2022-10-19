class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {"}":"{","]":"[",")":"("}
        for k in s:
            if k in open_to_close:
                if stack and (stack[-1] == open_to_close[k]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(k)
        if not stack : 
            return True
        else:
            return False
        