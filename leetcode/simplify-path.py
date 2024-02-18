class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        lst=path.split("/")
        for i in lst:
            if i=="..":
                if stack:
                    stack.pop()
            elif i=="" or i==".":
                pass
            else:
                stack.append(i)
        return "/"+"/".join(stack)
        
          
            
            

            
            
        