class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s):
            stack=[]
            helper={")":"("}
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
        res=[]
        path=[]
        def backtrack(path,opn,clos):
            if clos>opn:
                return 
            if len(path)==2*n:
                z="".join(path[:])
                if isValid(z):
                    res.append(z)
                return 
            path.append("(")
            backtrack(path,opn+1,clos)
            path.pop()
            path.append(")")
            backtrack(path,opn,clos+1)
            path.pop()
        backtrack([],0,0)
        return res

        