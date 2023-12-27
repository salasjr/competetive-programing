class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            iterable=nums2
            checker=nums1
        else:
            iterable=nums1
            checker=nums2
        d=Counter(checker)
        ans=[]
        for i in range(len(iterable)):
            if iterable[i] in checker and d[iterable[i]]:
                ans.append(iterable[i])
                d[iterable[i]]-=1
        return ans
                
                
                
            
            
        
        
       
        