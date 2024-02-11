class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        CountOneZero = [0] * n
        zero = 0
        count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                zero += 1
            if s[i] == '1':
                count += zero
            CountOneZero[i] = count        
        CountZeroOne = [0] * n
        one = 0
        count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                one += 1
            if s[i] == '0':
                count += one
            CountZeroOne[i] = count      
        ans = 0
        for i in range(n):
            if s[i] == '0':
                ans += CountOneZero[i]
            else:
                ans += CountZeroOne[i]     
        return ans

        
        
        


        
        