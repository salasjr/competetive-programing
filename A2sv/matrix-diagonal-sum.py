class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        for i in range(len(mat)):
            summ+=mat[i][i]
        for i in range(len(mat)):
            summ+=mat[i][len(mat)-i-1]
        a=len(mat)//2
        if len(mat)%2:
            return summ-mat[a][a]
        return summ
        
        