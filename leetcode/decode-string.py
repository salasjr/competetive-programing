class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        checker="1234567890"
        for i in s:
            if i !="]":
                stack.append(i)
            else:
                intt=""
                strr=""
                while stack[-1] !="[":
                    
                    strr=stack.pop()+strr
                stack.pop()
                while stack and (stack[-1] in checker):
                    intt=stack.pop()+intt
                num=int(intt)
                strr=num*strr
                stack.append(strr)
        return "".join(stack)


        