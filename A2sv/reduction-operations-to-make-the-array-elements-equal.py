class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        checker=set()
        count=0
        for i in range(len(nums)):
            if nums[i]==nums[0]:
                checker.add(nums[i])
                continue
            else:
                if nums[i] in checker:
                    count+=len(checker)-1
                else:
                    count+=len(checker)
                checker.add(nums[i])
        return count
                
                
            
            
        