from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        min_length = float('inf')
        q = deque()
        for i in range(n + 1):
            while q and prefix_sum[i] - prefix_sum[q[0]] >= k:
                min_length = min(min_length, i - q.popleft())
            while q and prefix_sum[i] <= prefix_sum[q[-1]]:
                q.pop()
            q.append(i)

        return min_length if min_length != float('inf') else -1

      
        
        
                



        