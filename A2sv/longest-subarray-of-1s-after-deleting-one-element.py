class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxlen=0
        left=0
        countzero=0
        for r in range(len(nums)):
            if nums[r]==0:
                countzero+=1
            while countzero>1:
                if nums[left]==0:
                    countzero-=1
                left+=1
            maxlen=max(maxlen,r-left)
            
        return maxlen
                    
       
                
                
            
        
                
                
        