class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        before = self.kthGrammar(n - 1, (k + 1) // 2)
        if before == 0:
            if k%2:
                return 0
            else:
                return 1
        else:
            if k%2:
                return 1
            else:
                return 0

            





        