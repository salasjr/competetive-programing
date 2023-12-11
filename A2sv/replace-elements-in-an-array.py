class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dictt={num:index for index,num in enumerate (nums)}
        for old,new in operations:
            index=dictt[old]
            nums[index]=new
            dictt[new]=index
        return nums
       
            
       
            
        