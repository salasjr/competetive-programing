class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1,len(nums)):
                if x+nums[j]== target:
                    list1.append(i)
                    list1.append(j)
                    return list1
            
    
            