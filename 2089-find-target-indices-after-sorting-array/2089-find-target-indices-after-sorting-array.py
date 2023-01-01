class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = sorted(nums)
        b=[]
        m = len(nums)
        for i in range(m):
            if a[i] == target:
                b.append(i)
        return b    
        
        
        
