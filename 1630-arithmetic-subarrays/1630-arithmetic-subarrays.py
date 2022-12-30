class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        A=[]
        m=len(l)
        for i in range(m):
            arr= nums[l[i]:(int(r[i])+1)]
            arr = sorted(arr)
            z=arr[1]-arr[0]
            y=True
            for j in range(2,len(arr)):
                if z!=arr[j]-arr[j-1]:
                    y=False
                    break
            A.append(y)
        return A
   
         

        

        
        