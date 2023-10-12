class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s="abcdefghijklmnopqrstuvwxyz"
        if target == "z":
            return letters[0]
        a=s.index(target)
        if target in letters:    
            b=letters.index(target)
            if len(letters)-1==b:
                return letters[0]
        for i in range(a+1,len(s)):
            if s[i] in letters:
                return s[i]
        return letters[0]
        