class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            lst=[]
            for j in range(len(matrix)):
                lst.append(matrix[j][i])
            ans.append(lst)
        return ans
                
        