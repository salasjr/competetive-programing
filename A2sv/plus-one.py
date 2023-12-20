class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_s=""
        for i in digits:
            num_s+=str(i)
        num=int(num_s)
        num+=1
        ans=str(num)
        ans2=[]
        for i in ans:
            ans2.append(int(i))
        return ans2
            
       

        
      
      
        
    