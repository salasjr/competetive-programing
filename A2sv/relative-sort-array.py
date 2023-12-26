class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_dict=Counter(arr1)
        arr_dict=Counter(arr2)
        ans=[]
        ans1=[]
        for i in range (len(arr2)):
            a=arr2_dict[arr2[i]]
            while a>0:
                ans.append(arr2[i])
                a-=1
        for i in range(len(arr1)):
            if arr1[i] not in arr_dict:
                ans1.append(arr1[i])
        ans1.sort()
        return ans+ans1
        
            
                
                
                
            
        