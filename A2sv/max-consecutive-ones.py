class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        k=0
        for i in nums:
            if i ==1:
                k+=1
            else:
                ans=max(ans,k)
                k=0
        ans = max(ans,k)
        return ans
        
        
                
            
                
            
        