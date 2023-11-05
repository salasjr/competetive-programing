class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        l, mx = n, float('-inf')

        for i, num in enumerate(nums):
            while stack and stack[-1][1] > num:
                cand = stack.pop()
                l = min(l, cand[0])
                mx = max(mx, cand[1])
            stack.append((i, num))

        if l == n:
            return 0

        r = n - 1 

        for i in range(n - 1, -1, -1):
            if nums[i] < mx:
                r = i
                break

        return r - l + 1

        
        
                
                
                
        