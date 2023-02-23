class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits)
        count=0
        list1=[]
        for i in range(x ):
            z=x-1
            y=digits[i]*10**z
            count+=y
            x-=1
        p=count+1
        for j in str(p):
            list1.append((j))       
        list1 = [int(i) for i in list1]
        return list1
        
      
      
        
    