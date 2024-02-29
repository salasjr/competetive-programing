class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return ""
        mydict={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],
                "5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],
               "9":["w","x","y","z"]
        }
        res=[]
        path=[]
        def backtrack(index, path):
            if index >= len(digits):
                res.append("".join(path))
                return 
            for letter in mydict[digits[index]]:
                path.append(letter)
                backtrack(index+1,path)
                path.pop()

        backtrack(0,[])

        return res



        