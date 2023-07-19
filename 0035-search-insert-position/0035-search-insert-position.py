class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        while right>=left:
            mid = left +(right-left)//2
            if nums[mid] > target:
                right-=1
            elif nums[mid] < target:
                left  +=1
            else:
                return mid
            
        return left
                
            
                
            
       
        