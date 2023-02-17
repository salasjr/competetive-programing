class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        z,total=0,0
        res = float("inf")
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                res= min(i+1-z,res)
                total-=nums[z]
                z+=1
        return 0 if res== float("inf") else res
                
        