class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums),2):
            a,b=nums[i],nums[i+1]
            ans+=[b]*a
        return ans
        