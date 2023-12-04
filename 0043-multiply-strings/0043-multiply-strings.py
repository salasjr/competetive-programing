class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        ans1=""
        ans2=""
        for i in num1:
            ans1+=str(d[i])
        for j in num2:
            ans2+=str(d[j])
        z=int(ans1)*int(ans2)
        return str(z) 
            
        