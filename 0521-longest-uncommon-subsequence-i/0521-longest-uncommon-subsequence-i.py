class Solution:
    def findLUSlength(self, A, B):
        if A == B:
            return -1
        return max(len(A), len(B))

