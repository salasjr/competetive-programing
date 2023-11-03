class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and i==stack[-1]:
                stack.append(i)
            elif (stack and i==stack[-1].upper()):
                stack.pop()
            elif stack and i.upper() == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        