class Solution:
    def sortColors(self, nums: List[int]) -> None:
        s= Counter(nums)
        i=0
        for i in range(len(nums)):
            if s[0]:
                nums[i]=0
                s[0]-=1
            elif s[1]:
                nums[i]=1
                s[1]-=1
            else:
                nums[i]=2
                s[2]-=1
            i+=1
        return nums
        
                
                
        
            
       