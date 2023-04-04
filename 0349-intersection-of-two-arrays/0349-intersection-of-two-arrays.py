import numpy
class Solution:
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # i,j = 0,0
        # result=[]
        # nums1,nums2 = sorted(nums1),sorted(nums2)
        # while i<len(nums1) and j < len(nums2):
        #     if nums1[i]<nums2[j]:
        #         i+1
        #     elif nums2[j]<nums1[i]:
        #         j+1
        #     else:
        #         result.append(nums1[i])
        #         j+=1
        #         i+=1
        # return result
        
        count=Counter(nums1)
        result=[]
        for n in nums2:
            if count[n]>0:
                result.append(n)
                count[n]=count[n]-1
       
        return numpy.unique(result)
                
        
      