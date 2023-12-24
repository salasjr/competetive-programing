class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker=[".",".",".",".",".",".",".",".","."]
        def validaterow(arr):
            count=Counter(arr)
            for a ,b in count.items():
                if b>1 and a !=".":
                    return False
            return True
        def validatecolumn(arr):
            for i in range(len(arr[0])):
                ans=[]
                j=0
                while j <9:
                    ans.append(arr[j][i])
                    j+=1
                if not validaterow(ans):
                    return False
            return True
        ans=True
        for i in range(len(board)):
            if ans==False:
                return False
            ans=validaterow(board[i])   
        if ans==False:
            return False  
        ans=validatecolumn(board)
        for i in range(0, 9, 3):  
            for j in range(0, 9, 3):  
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not validaterow(sub_box):
                    return False
        return ans
        
        
                
    
       
        
       
        
        
                
                    
            
            
        
        