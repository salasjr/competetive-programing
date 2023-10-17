class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn=float('inf')
        ans=[]
        for i in range(len(arr)-1):
            minn=min(minn,arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minn:
                ans.append([arr[i],arr[i+1]])
        return ans
            
        