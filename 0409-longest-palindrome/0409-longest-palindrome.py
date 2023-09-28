class Solution:
    def longestPalindrome(self, s: str) -> int:
        strr= Counter(s)
        count=0
        flag = False
        print(strr)
        for a,b in strr.items():
            if len(strr) ==1:
                return b
            if b>1 and b%2==0:
                count+=b
            if b>1 and b%2!=0:
                count+=b-1
                flag = True
            if b ==1:
                flag = True
                
        if flag:
            return count+1
        return count
    
     
            
        