class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        maxx=max(arr)
        index=arr.index(maxx)
        ans=True
        if index == len(arr)-1 or index==0:
            return False
        for i in range(index):
            if arr[i]>=arr[i+1]:
                ans=False
        for i in range(index,len(arr)-1):
            if arr[i]<=arr[i+1]:
                ans=False
        return ans
        
       
        
        