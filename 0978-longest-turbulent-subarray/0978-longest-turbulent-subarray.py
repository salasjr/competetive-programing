class Solution(object):
    def maxTurbulenceSize(self, A):
        
        def compute(a,b):
            return (a-b)//abs(a-b) if a-b else 0
            
        N = len(A)
        ans = 1
        l = 0

        for r in range(1, N):
            c = compute(A[r-1], A[r])
            if c == 0:
                l = r
            elif r == N-1 or c * compute(A[r], A[r+1]) != -1:
                ans = max(ans, r - l + 1)
                l = r
        return ans