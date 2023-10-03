class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        newst = str(num)
        l =0
        r =k
        count =0
        while r <= len(newst):
            a= newst[l:r]
            if a != '0' * len(a):
                num1 = a.lstrip('0')
            else:
                num1=0
            num2 =int(num1)
            if num2 == 0:
                count=count
            elif num%num2 ==0:
                count+=1  
            l+=1
            r+=1
        return count
        
       
            
            
        
            
        