class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        n=len(self.matrix[0])
        m=len(self.matrix)
        self.pre=[]
        self.pre=[[0 for col in range(n+1)] for row in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + self.matrix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        z= self.pre[row2+1][col2+1] - self.pre[row2+1][col1] - self.pre[row1][col2 +1] + self.pre[row1][col1]
        return z
        


# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)