class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        visted=collections.Counter()
        n=len(nums)
        maxx=0
        curr=0
        for r in range(n):
            visted[nums[r]]+=1
            curr+=nums[r]
            if r-k>=0:
                visted[nums[r-k]]-=1
                if visted[nums[r-k]]==0:
                    del visted[nums[r-k]]
                curr-=nums[r-k]
            if r-k+1>=0:
                if len(visted)==k:
                    maxx=max(curr,maxx)
        return maxx
       
           
        