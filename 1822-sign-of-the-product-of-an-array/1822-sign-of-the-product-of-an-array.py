class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=0
        y=0
        for i in range(len(nums)):
            if nums[i]==0:
                return 0
            if nums[i]>0:
                x+=1
            if nums[i]<0:
                y+=1
        if y%2==0:
            return 1
        return -1
      
        