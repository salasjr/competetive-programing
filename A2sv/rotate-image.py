class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix[0])):
            for j in range(i,len(matrix)):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        
        