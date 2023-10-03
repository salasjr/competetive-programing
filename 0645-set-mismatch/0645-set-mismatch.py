class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        s1= sorted(s.items())
        for i in range(1, len(nums)+1):
            if i not in s:
                missing = i
            elif s[i] == 2:
                duplicate = i
        return[duplicate,missing]
        
                
        