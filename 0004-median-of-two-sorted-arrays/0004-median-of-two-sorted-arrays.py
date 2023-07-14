class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        z= (len(nums1)//2)-1
        if len(nums1) %2 ==0:
            return (nums1[z] + nums1[z+1])/2
        return float(nums1[len(nums1)//2])
        