class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        n=len(nums)
        l,r=n,0
        for a,b in enumerate(nums):
            if nums[a]!=nums1[a]:
                l=min(l,a)
                r=max(r,a)
        if l==n:return 0
        else:
            return r-l+1
            
    
                
                
                
        