class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(15000)
        ans=[]
        st="".join(map(str,num))
        z= int(st)+k
        while z > 0:
            a= z%10
            ans.append(a)
            z=z//10
        ans1=ans[::-1]
        return ans1
            
        
        
        