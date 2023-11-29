class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>1:
            a=n%3
            if a ==1:
                n=(n-1)//3
            elif a==0:
                n=n//3
            elif a==4:
                n=(n-4)//3
            else:
                return False
        return True



        
        

        